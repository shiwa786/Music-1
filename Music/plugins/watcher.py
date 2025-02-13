import asyncio
import datetime

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from pyrogram import filters
from pyrogram.types import Message

from config import Config
from Music.core.calls import hellmusic
from Music.core.clients import hellbot
from Music.core.database import db
from Music.core.logger import LOGS
from Music.helpers.buttons import Buttons
from Music.utils.leaderboard import leaders
from Music.utils.queue import Queue


@hellbot.app.on_message(filters.private, group=2)
async def new_users(_, msg: Message):
    chat_id = msg.from_user.id
    if not await db.is_user_exist(chat_id):
        BOT_USERNAME = hellbot.app.username
        await db.add_user(chat_id, msg.from_user.first_name)
        if Config.LOGGER_ID:
            await hellbot.logit(
                "newuser",
                f"**⤷ User:** {msg.from_user.mention(style='md')}\n**⤷ ID:** `{msg.from_user.id}`\n__⤷ Started @{BOT_USERNAME} !!__",
            )
        else:
            LOGS.info(
                f"#NewUser: \n\nName: {msg.from_user.first_name} \nID: {msg.from_user.id}"
            )
    await msg.continue_propagation()


@hellbot.app.on_message(filters.group, group=3)
async def new_users(_, msg: Message):
    chat_id = msg.chat.id
    if not await db.is_chat_exist(chat_id):
        BOT_USERNAME = hellbot.app.username
        await db.add_chat(chat_id)
        if Config.LOGGER_ID:
            await hellbot.logit(
                "newchat",
                f"**⤷ Chat Title:** {msg.chat.title} \n**⤷ Chat UN:** @{msg.chat.username or None}) \n**⤷ Chat ID:** `{chat_id}` \n__⤷ ADDED @{BOT_USERNAME} !!__",
            )
        else:
            LOGS.info(
                f"#NEWCHAT: \n\nChat Title: {msg.chat.title} \nChat UN: @{msg.chat.username}) \nChat ID: {chat_id} \n\nADDED @{BOT_USERNAME} !!",
            )
    await msg.continue_propagation()


async def update_played():
    while not await asyncio.sleep(1):
        active_chats = await db.get_active_vc()
        for x in active_chats:
            chat_id = int(x["chat_id"])
            if chat_id == 0:
                continue
            is_paused = await db.get_watcher(chat_id, "pause")
            if is_paused:
                continue
            que = Queue.get_queue(chat_id)
            if que == []:
                continue
            Queue.update_duration(chat_id, 1, 1)


asyncio.create_task(update_played())


async def end_inactive_vc():
    while not await asyncio.sleep(10):
        for chat_id in db.inactive:
            dur = db.inactive.get(chat_id)
            if dur == {}:
                continue
            if datetime.datetime.now() > dur:
                if not await db.is_active_vc(chat_id):
                    db.inactive[chat_id] = {}
                    continue
                db.inactive[chat_id] = {}
                try:
                    await hellmusic.leave_vc(chat_id)
                except:
                    continue
                try:
                    await hellbot.app.send_message(
                        chat_id,
                        "⏹️ **Inactive VC:** Streaming has been stopped!",
                    )
                except:
                    continue


asyncio.create_task(end_inactive_vc())


async def leaderboard():
    context = {
        "mention": hellbot.app.mention,
        "username": hellbot.app.username,
        "client": hellbot.app,
    }
    text = await leaders.generate(context)
    btns = Buttons.close_markup()
    await leaders.broadcast(hellbot, text, btns)


scheduler = AsyncIOScheduler()
scheduler.add_job(leaderboard, "cron", hour=3, minute=45, timezone=Config.TZ)
scheduler.start()
