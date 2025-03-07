import os
from distutils.util import strtobool
from os import getenv
from X.helpers.cmd import cmd
from dotenv import load_dotenv

load_dotenv("config.env")

ALIVE_EMOJI = getenv("ALIVE_EMOJI", "⚡")
ALIVE_LOGO = getenv("ALIVE_LOGO", "https://telegra.ph/file/71fcc97ea73c5265d6925.jpg")
ALIVE_TEKS_CUSTOM = getenv("ALIVE_TEKS_CUSTOM", "𝐇ᴇʏ , 𝐃ɪᴄᴛᴀᴛᴏʀ 𝐔sᴇʀ𝐁ᴏᴛ 𝐈s 𝐀ʟɪᴠᴇ 🥀")
API_HASH = getenv("API_HASH", "34efb38c74d5e6b25d1bb6234396a8af")
API_ID = getenv("API_ID", "23129036")
BOTLOG_CHATID = int(getenv("BOTLOG_CHATID") or 0)
BOT_VER = "3.0.0@main"
BRANCH = getenv("BRANCH", "main") #don't change this line 
CMD_HNDLR = cmd
OWNER_ID = getenv("OWNER_ID", "8181241262")
BOT_TOKEN = getenv("BOT_TOKEN", "none")
OPENAI_API_KEY = getenv("OPENAI_API_KEY", "")
CHANNEL = getenv("CHANNEL", "SAIFALLBOT")
CMD_HANDLER = getenv("CMD_HANDLER", ".")
DB_URL = getenv("DATABASE_URL", "mongodb+srv://sujoy123m:wTWKGUaxYE7dxb1l@cluster0.zorxb.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
GIT_TOKEN = getenv("GIT_TOKEN", "")
GROUP = getenv("GROUP", "DEAD_GRPCHAT")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
PMPERMIT_PIC = getenv("PMPERMIT_PIC", "https://telegra.ph/file/d18514b209f6cca4b1ae0.jpg")
PM_AUTO_BAN = strtobool(getenv("PM_AUTO_BAN", "False"))
REPO_URL = getenv("REPO_URL", "https://github.com/SAIFDEAD/USERBOT")
STRING_SESSION1 = getenv("STRING_SESSION1", "BQFSeS0AHUos7Cc50omrczdKvFK9Cvhe9VTNZ81Vy6NpC_oBWkSg2fzpYJjac2ILIqxgs7bTuZzyKf4vQF_D4HLrzWvncb048kTNwRCiRQ6Qg4ymmNjei2Q6Enm3Y3jvmkYDV8V8Af1HezNjVpI_8qmcnCX4_hscUIrPycKLiwP9HmJFVgwevoYJFhto5VDnn315kHsqfjQL9HOp_7xCBmK_PlqIMRSBtqwhVuWxrLzm6LuVczwMbRykh6K8q7EKM3YQlejxtz4Y152jzFoI6KTXFbOkATgEViyIh0i5VMqe24gVwcx-QF9SgNGrfwi1V9ZAYKTaC1Wzlc99VcHvtBbPCaMbzwAAAAHTfySqAA")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
STRING_SESSION6 = getenv("STRING_SESSION6", "")
STRING_SESSION7 = getenv("STRING_SESSION7", "")
STRING_SESSION8 = getenv("STRING_SESSION8", "")
STRING_SESSION9 = getenv("STRING_SESSION9", "")
STRING_SESSION10 = getenv("STRING_SESSION10", "")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "7117906157").split()))
BLACKLIST_CHAT = getenv("BLACKLIST_CHAT", None)
if not BLACKLIST_CHAT:
    BLACKLIST_CHAT = [-1002038548340, -1002131043993, -1002123837285]
BLACKLIST_GCAST = {int(x) for x in getenv("BLACKLIST_GCAST", "").split()}
