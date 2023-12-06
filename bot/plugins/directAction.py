import os
import logging
from pyrogram import filters as Filters
from pyrogram import enums
from pyrogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    Message,
    CallbackQuery,
)

from ..youtube import GoogleAuth
from ..config import Config
from ..translations import Messages as tr
from ..utubebot import UtubeBot
import httplib2


log = logging.getLogger(__name__)

auth = GoogleAuth(Config.CLIENT_ID, Config.CLIENT_SECRET)
url = auth.GetAuthUrl()


@UtubeBot.on_callback_query(
    Filters.create(lambda _, __, query: query.data.startswith("cncl+"))
)
async def cncl(c: UtubeBot, q: CallbackQuery) -> None:
    _, pid = q.data.split("+")
    if not c.download_controller.get(pid, False):
        await q.answer("Your process is not currently active!", show_alert=True)
        return
    c.download_controller[pid] = False
    await q.answer("Your process will be cancelled soon!", show_alert=True)


@UtubeBot.on_callback_query(
    Filters.create(lambda _, __, query: query.data.startswith("logout"))
)
async def _logout(c: UtubeBot, q: CallbackQuery) -> None:
    try:
        auth.LoadCredentialsFile(Config.CRED_FILE(q.from_user.id))
        auth.revoke()
        os.remove(Config.CRED_FILE(q.from_user.id))
        await c.send_chat_action(q.id, enums.ChatAction.TYPING)
        await q.edit_message_text(
            text=tr.LOGOUT_SUCCESS_MSG,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text="🌎 SIGN UP WITH GOOGLE 🌎", url=url
                        )
                    ],
                    [
                        InlineKeyboardButton(
                            text="Visit Website!💫", url="https://lethargic-sol.netlify.app"
                        ),
                        InlineKeyboardButton(
                            text="Help and Support😌", url="https://t.me/LethargicBots"
                        ),
                    ],
                    [
                        InlineKeyboardButton(
                            "Help Book📚",
                            callback_data="help+1",
                        )
                    ]
                ]
            ),
        )
    except Exception as e:
        log.error(e, exc_info=True)
        await q.edit_message_text(text=tr.LOGOUT_FAILED_MSG,
                                  disable_web_page_preview=True,
                                  reply_markup=InlineKeyboardMarkup(
                                      [
                                          [
                                              InlineKeyboardButton(
                                                  text="🌎 SIGN IN WITH GOOGLE 🌎", url=url
                                              )
                                          ],
                                          [
                                              InlineKeyboardButton(
                                                  "Help Book📚",
                                                  callback_data="help+1",
                                              )
                                          ]
                                      ]
                                  ),
                                  )
