from os import path, getenv
from dotenv import load_dotenv

if path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()

class zaid (object):
        admins = {}
        BOT_TOKEN = getenv("BOT_TOKEN", None)
        API_ID = int(getenv("API_ID", "6"))
        API_HASH = getenv("API_HASH", "4e984ea35f854762dcde906dce426c2d")
        SESSION_NAME = getenv("SESSION_NAME", None)
        DURATION_LIMIT = int(getenv("DURATION_LIMIT", "15"))
        SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
        ASSISTANT_NAME = getenv("ASSISTANT_NAME", "Zaid_Assistant")
        BOT_USERNAME = getenv("BOT_USERNAME", "ZAID_VD_BOT")
        COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
        FPS = int(getenv('FPS', 20))
        WIDTH = int(getenv('WIDTH', 1280))
        HEIGHT = int(getenv('HEIGHT', 720))
        BITRATE = int(getenv('BITRATE', 48000))
