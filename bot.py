from pyrogram import Client

from config import Config


plugins = dict(
    root="plugins",
    include=[
        "start",
        "help",
        "authentication",
        "upload"
    ]
)


Client('youtube-upload', bot_token = Config.BOT_TOKEN,
    api_id = Config.API_ID, api_hash = Config.API_HASH,
    plugins = plugins, workers = 6
).run()
