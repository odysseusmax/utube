import logging
import os
from pyrogram import filters as Filters
from pyrogram.types import Message
from ..youtube import GoogleAuth
from ..config import Config
from ..translations import Messages as tr
from ..utubebot import UtubeBot

from pyrogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    Message,
    CallbackQuery,
)

log = logging.getLogger(__name__)


@UtubeBot.on_message(
    Filters.private
    & Filters.incoming
    & Filters.command("auth")
    & Filters.user(Config.AUTH_USERS)
)
async def _auth(c: UtubeBot, m: Message) -> None:
    if len(m.command) == 1:
        await m.reply_text(tr.NO_AUTH_CODE_MSG, True)
        return

    code = m.command[1]

    try:
        auth = GoogleAuth(Config.CLIENT_ID, Config.CLIENT_SECRET)
        auth.Auth(code)
        auth.SaveCredentialsFile(Config.CRED_FILE(m.chat.id))

        msg1 = await m.reply_text(tr.AUTH_SUCCESS_MSG, True)
        msg2 = await msg1.reply_text(tr.AUTH_DATA_SAVE_SUCCESS, True)

    except Exception as e:
        log.error(e, exc_info=True)
        await m.reply_text(tr.AUTH_FAILED_MSG.format(e), True)

