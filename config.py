import os

class Config:

    BOT_TOKEN = os.getenv("BOT_TOKEN", "")                                    # Get From https://t.me/BotFather

    API_ID = int(os.getenv("API_ID", 123456))                                 # Get from https://my.telegram.org/apps

    API_HASH = os.getenv("API_HASH", "")                                      # Get from https://my.telegram.org/apps

    CLIENT_ID = os.getenv("CLIENT_ID", "")                                    # Get from https://console.developers.google.com/apis/credentials

    CLIENT_SECRET = os.getenv("CLIENT_SECRET", "")                            # Get from https://console.developers.google.com/apis/credentials

    BOT_OWNER = int(os.getenv("BOT_OWNER", 374321319))                        # Bot owner's telegram id

    AUTH_USERS = [BOT_OWNER,374321319]+[int(user) for user in os.environ["AUTH_USERS"].split(",")]
                                                                              # Id of other users who want to use your bot

    CRED_FILE = "auth_token.txt"                                              # Credentials file



