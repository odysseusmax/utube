from pyrogram import Filters

from ..utubebot import UtubeBot
from ..config import Config


@UtubeBot.on_message(
    Filters.private 
    & Filters.incoming
    & ~Filters.user(Config.AUTH_USERS)
)
async def _non_auth_usr_msg(c, m):
    await m.delete(True)
