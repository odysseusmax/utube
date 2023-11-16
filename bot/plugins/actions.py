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


def map_btns(pos):
    if pos == 1:
        button = [[InlineKeyboardButton(text="⏩", callback_data="help+2")]]
    elif pos == len(tr.HELP_MSG) - 1:
        button = [
            [InlineKeyboardButton(text="⏪", callback_data=f"help+{pos-1}")],
            [InlineKeyboardButton(text="🌎 SIGN UP WITH GOOGLE 🌎🌎🌎", url=url)],
        ]
    else:
        button = [
            [
                InlineKeyboardButton(
                    text="⏪", callback_data=f"help+{pos-1}"),
                InlineKeyboardButton(
                    text="⏩", callback_data=f"help+{pos+1}"),
            ],
        ]
    return button


@UtubeBot.on_message(
    Filters.private
    & Filters.incoming
    & Filters.command("help")
    & Filters.user(Config.AUTH_USERS)
)
async def _help(c: UtubeBot, m: Message):
    await c.send_chat_action(m.chat.id, enums.ChatAction.TYPING)
    await m.reply_text(
        text=tr.HELP_MSG[1],
        reply_markup=InlineKeyboardMarkup(map_btns(1)),
    )


help_callback_filter = Filters.create(
    lambda _, __, query: query.data.startswith("help+")
)


@UtubeBot.on_callback_query(help_callback_filter)
async def help_answer(c: UtubeBot, q: CallbackQuery):
    pos = int(q.data.split("+")[1])
    await q.answer()
    await q.edit_message_text(
        text=tr.HELP_MSG[pos], reply_markup=InlineKeyboardMarkup(map_btns(pos))
    )


# login command added

@UtubeBot.on_message(
    Filters.private
    & Filters.incoming
    & Filters.command("login")
    & Filters.user(Config.AUTH_USERS)
)
async def _login(c: UtubeBot, m: Message):
    await c.send_chat_action(m.chat.id, enums.ChatAction.TYPING)

    await m.reply_text(
        text=tr.LOGIN_MSG,
        quote=True,
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton(text="🌎 SIGN IN WITH GOOGLE 🌎", url=url)]]
        ),
    )

# Refresh Command added.


@UtubeBot.on_message(
    Filters.private
    & Filters.incoming
    & Filters.command("refresh")
    & Filters.user(Config.AUTH_USERS)
)
async def _refresh(c: UtubeBot, m: Message) -> None:
    try:
        auth.LoadCredentialsFile(Config.CRED_FILE(m.chat.id))
        auth.credentials.refresh(httplib2.Http())
        auth.SaveCredentialsFile(Config.CRED_FILE(m.chat.id))
        await m.reply_text(tr.TOKEN_REFRESH_SUCCESS_MSG, True)
    except Exception as e:
        log.error(e, exc_info=True)
        await m.reply_text(tr.TOKEN_REFRESH_NOT_FOUND_OR_NOTEXPIRED_MSG, quote=True,
                           disable_web_page_preview=True,
                           reply_markup=InlineKeyboardMarkup(
                               [
                                   [
                                       InlineKeyboardButton(
                                           text="Logout", callback_data='logout'
                                       )
                                   ],
                                   [
                                       InlineKeyboardButton(
                                           text="🌎Login🌎", url=url
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

# logout command added


@UtubeBot.on_message(
    Filters.private
    & Filters.incoming
    & Filters.command("logout")
    & Filters.user(Config.AUTH_USERS)
)
async def _logout(c: UtubeBot, m: Message):
    try:
        auth.LoadCredentialsFile(Config.CRED_FILE(m.chat.id))
        auth.revoke()
        os.remove(Config.CRED_FILE(m.chat.id))
        await c.send_chat_action(m.chat.id, enums.ChatAction.TYPING)
        await m.reply_text(
            text=tr.LOGOUT_SUCCESS_MSG,
            quote=True,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text="🌎 SIGN IN🌎", url=url
                        )
                    ],
                    [
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
    except FileNotFoundError:
        await m.reply_text("You have not logged in yet.", True)
    except Exception as e:
        log.error(e, exc_info=True)
        await m.reply_text(text=tr.LOGOUT_FAILED_MSG,
                           quote=True,
                           disable_web_page_preview=True,
                           reply_markup=InlineKeyboardMarkup(
                               [
                                   [
                                       InlineKeyboardButton(
                                           text="🌎 SIGN IN🌎", url=url
                                       )
                                   ], [
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

