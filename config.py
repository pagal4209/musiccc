import config
import os
import re
from os import getenv
from dotenv import load_dotenv
from pyrogram import filters
import random
from pyrogram import filters
from dotenv import load_dotenv

load_dotenv()

# ----------- REQUIRED CONFIG ------------ #

API_ID = int(os.getenv("API_ID", "21189715"))
API_HASH = os.getenv("API_HASH", "988a9111105fd2f0c5e21c2c2449edfd")

BOT_TOKEN = os.getenv("BOT_TOKEN", "8540734638:AAFacsmtuX8IrgrviLeybxfLlkkM4_dgjeM")

MONGO_DB_URI = os.getenv(
    "MONGO_DB_URI",
    "mongodb+srv://Ashiku:ashachiku123@cluster0.wu7maqj.mongodb.net/?retryWrites=true&w=majority"
)

LOGGER_ID = int(os.getenv("LOGGER_ID", "-1001956979385"))
OWNER_ID = int(os.getenv("OWNER_ID", "8111174619"))

BOT_USERNAME = os.getenv("BOT_USERNAME", "ashababybot")

COMMAND_HANDLER = os.getenv("COMMAND_HANDLER", "! . /").split()

# ----------- HEROKU CONFIG ------------ #

HEROKU_APP_NAME = os.getenv("HEROKU_APP_NAME", "")
HEROKU_API_KEY = os.getenv("HEROKU_API_KEY", "")

# ----------- REPO CONFIG ------------ #

UPSTREAM_REPO = os.getenv("UPSTREAM_REPO", "https://github.com/ayanokozii/Sifra2")
UPSTREAM_BRANCH = os.getenv("UPSTREAM_BRANCH", "Anya")
GIT_TOKEN = os.getenv("GIT_TOKEN", "")

# ----------- SUPPORT ------------ #

SUPPORT_CHANNEL = os.getenv("SUPPORT_CHANNEL", "https://t.me/MyParadisebots")
SUPPORT_CHAT = os.getenv("SUPPORT_CHAT", "https://t.me/+sZkceL-QH0U1N2Y1")

# ----------- API SETTINGS ------------ #

API_URL = os.getenv("API_URL", "https://api.thequickearn.xyz")
VIDEO_API_URL = os.getenv("VIDEO_API_URL", "https://api.video.thequickearn.xyz")
API_KEY = os.getenv("API_KEY", "30DxNexGenBotsf899eb")

AUTO_LEAVING_ASSISTANT = bool(os.getenv("AUTO_LEAVING_ASSISTANT", False))
AUTO_SUGGESTION_MODE = os.getenv("AUTO_SUGGESTION_MODE", "True")
AUTO_SUGGESTION_TIME = int(os.getenv("AUTO_SUGGESTION_TIME", "500"))

# ----------- SPOTIFY ------------ #

SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID", "")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET", "")

PLAYLIST_FETCH_LIMIT = int(os.getenv("PLAYLIST_FETCH_LIMIT", 25))

# ----------- CLEAN MODE ------------ #

CLEANMODE_DELETE_MINS = int(os.getenv("CLEANMODE_MINS", "5"))

TG_AUDIO_FILESIZE_LIMIT = int(os.getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(os.getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))

# ----------- STRINGS ------------ #

STRING1 = os.getenv("STRING_SESSION", "BQGuP2cAcVFXMnABWTBehebZzDZ_qgvpk07P-yT0wAq0zaWYbUiPS6ud5sh6RC_56So-L42u29MDYoqA2t-iJ-pdC5ijEE_QKjD6iAul6LHRH9Sle6kHZg_pLCgmHr-UgUAmf8-a86k2IoQhY9MSvyeMTL--yvyG24BwAe1FU0rMRkzxjLWhP6DfZ7bULUX50H6Twbki18ie2UitIHOuGxzRCran9JvFsclKxBRovGqTm8y_WD1EUB6SdWD8O-_hA-uLRXkAm4NlQNElUTFG4VOs4E4SkP5d3-UQIu0CX0-4RJUcm3PnAtvgtul1GU8Eum3yQAnUX1k-wnAl7_ITBFLHO0tRYgAAAAHPtvqPAA")
STRING2 = os.getenv("STRING_SESSION2", "")
STRING3 = os.getenv("STRING_SESSION3", "")
STRING4 = os.getenv("STRING_SESSION4", "")
STRING5 = os.getenv("STRING_SESSION5", "")


# ------------------------- INTERNAL LISTS -------------------------

BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
autoclean = []
votemode = {}
confirmer = {}
chatstats = {}
userstats = {}
clean = {}

# ------------------------- IMAGES -------------------------

START_IMAGES = [
    "https://telegra.ph/file/faf065e6f231437ddb0c7.jpg",
    "https://telegra.ph/file/d08a9f47092fa91f54f3b.jpg",
    "https://telegra.ph/file/81df44f3679946babd8c3.jpg",
]

START_IMG_URL = random.choice(START_IMAGES)

PING_IMG_URL = os.getenv("PING_IMG_URL", "https://telegra.ph/file/d08a9f47092fa91f54f3b.jpg")
PLAYLIST_IMG_URL = "https://telegra.ph/file/faf065e6f231437ddb0c7.jpg"
STATS_IMG_URL = "https://telegra.ph/file/faf065e6f231437ddb0c7.jpg"
TELEGRAM_AUDIO_URL = "https://telegra.ph/file/81df44f3679946babd8c3.jpg"
TELEGRAM_VIDEO_URL = "https://telegra.ph/file/d08a9f47092fa91f54f3b.jpg"
STREAM_IMG_URL = "https://telegra.ph/file/d08a9f47092fa91f54f3b.jpg"
SOUNCLOUD_IMG_URL = "https://telegra.ph/file/d08a9f47092fa91f54f3b.jpg"
YOUTUBE_IMG_URL = "https://telegra.ph/file/81df44f3679946babd8c3.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://telegra.ph/file/faf065e6f231437ddb0c7.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://telegra.ph/file/d08a9f47092fa91f54f3b.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://telegra.ph/file/faf065e6f231437ddb0c7.jpg"

# ------------------------- TIME CONVERT -------------------------

def time_to_seconds(time):
    t = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(t.split(":"))))


DURATION_LIMIT_MIN = int(os.getenv("DURATION_LIMIT", "54000"))
SONG_DOWNLOAD_DURATION = int(os.getenv("SONG_DOWNLOAD_DURATION_LIMIT", "54000"))

DURATION_LIMIT = time_to_seconds(f"{DURATION_LIMIT_MIN}:00")
SONG_DOWNLOAD_DURATION_LIMIT = time_to_seconds(f"{SONG_DOWNLOAD_DURATION}:00")


# ------------------------- URL VALIDATION -------------------------

if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
