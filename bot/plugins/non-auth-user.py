from pyrogram import Filters

from ..utubebot import UtubeBot
from ..config import Config


@UtubeBot.on_message(
    Filters.private 
    & Filters.incoming
    & ~Filters.user(Config.AUTH_USERS)
)
def _non_auth_usr_msg(c, m):
    m.delete(True)
