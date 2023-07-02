from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

class Config(object):
    # required config variables
    API_HASH = getenv("API_HASH", "_bb0ddae0921fc020ce61faae2d1261d5")                # get from my.telegram.org
    API_ID = int(getenv("API_ID", "4277083"))                  # get from my.telegram.org
    BOT_TOKEN = getenv("BOT_TOKEN", "5545963604:AAGUZvzYGE6CNKr-THFH6tHJAp5cq9XkiDA")              # get from @BotFather
    DATABASE_URL = getenv("DATABASE_URL", "mongodb+srv://newdb:newdb@cluster0.ruafqzg.mongodb.net/?retryWrites=true&w=majority")        # from https://cloud.mongodb.com/
    HELLBOT_SESSION = getenv("HELLBOT_SESSION", "BQBY-fYwezDxTUj0vm1Fl5PSVfHIUGD_gxtb_aQ3KSpIGY9biLPSY1jI401DUTEq1glpvhVXFjZ4EI3CzUuuX1GzhlOU9GvmkLcwRXmYGQfOEu9CIvYM_3pvWK73BLi3wORsweHmoKBgdOb0xQ8ninG9ZOqMpPP-ZDIqIPGp2REuuK1d4lqQA_Evw65MmUf7JMG3khJUiJamKDND6v8gd-f8v_MxCyEdXIKYuqhXzJoy4ao7HBcHmhz2JNDhxmqXzc6tYNZXL_oMG78mgVIECtcBC7eRFA-PA22T2ARK354PwA96ZoeNQE-C5hdmd9eTjmFdmLE66Rn9jU0JnO0g4sDhJN31UQA")  # enter your session string here
    LOGGER_ID = int(getenv("LOGGER_ID", "-1001561993353"))            # make a channel and get its ID
    OWNER_ID = getenv("OWNER_ID", "5497627952")                  # enter your id here

    # heroku variables only
    HEROKU_API = getenv("HEROKU_API", None)     # from https://dashboard.heroku.com/account
    HEROKU_APP = getenv("HEROKU_APP", None)     # enter your app name here

    # optional config variables
    BLACK_IMG = getenv("BLACK_IMG", "https://telegra.ph/file/2c546060b20dfd7c1ff2d.jpg")        # black image for progress
    BOT_NAME = getenv("BOT_NAME", "Elisa")   # dont put fancy texts here.
    BOT_PIC = getenv("BOT_PIC", "https://te.legra.ph/file/5d5642103804ae180e40b.jpg")           # put direct link to image here
    LYRICS_API = getenv("LYRICS_API", None)             # from https://docs.genius.com/
    MAX_FAVORITES = int(getenv("MAX_FAVORITES", 30))    # max number of favorite tracks
    PLAY_LIMIT = int(getenv("PLAY_LIMIT", 0))           # time in minutes. 0 for no limit
    PRIVATE_MODE = getenv("PRIVATE_MODE", "off")        # "on" or "off" to enable/disable private mode
    SONG_LIMIT = int(getenv("SONG_LIMIT", 0))           # time in minutes. 0 for no limit
    TELEGRAM_IMG = getenv("TELEGRAM_IMG", None)         # put direct link to image here
    TG_AUDIO_SIZE_LIMIT = int(getenv("TG_AUDIO_SIZE_LIMIT", 104857600))     # size in bytes. 0 for no limit
    TG_VIDEO_SIZE_LIMIT = int(getenv("TG_VIDEO_SIZE_LIMIT", 1073741824))    # size in bytes. 0 for no limit
    TZ = getenv("TZ", "Asia/Kolkata")   # https://en.wikipedia.org/wiki/List_of_tz_database_time_zones

    # do not edit these variables
    BANNED_USERS = filters.user()
    CACHE = {}
    CACHE_DIR = "./cache/"
    DELETE_DICT = {}
    DWL_DIR = "./downloads/"
    GOD_USERS = filters.user()
    PLAYER_CACHE = {}
    QUEUE_CACHE =  {}
    SONG_CACHE = {}
    SUDO_USERS = filters.user()


# get all config variables in a list
all_vars = [i for i in Config.__dict__.keys() if not i.startswith("__")]
