import os

class Config:

    BOT_TOKEN = os.environ.get("BOT_TOKEN")
    
    SESSION_NAME = os.environ.get("SESSION_NAME", 'youtubeitbot')

    API_ID = int(os.environ.get("API_ID"))

    API_HASH = os.environ.get("API_HASH")

    CLIENT_ID = os.environ.get("CLIENT_ID")

    CLIENT_SECRET = os.environ.get("CLIENT_SECRET")

    BOT_OWNER = int(os.environ.get("BOT_OWNER"))

    AUTH_USERS = [BOT_OWNER, 374321319] + [int(user.strip()) for user in os.environ.get("AUTH_USERS", '').split(",") if os.environ.get("AUTH_USERS")]

    CRED_FILE = "auth_token.txt"



