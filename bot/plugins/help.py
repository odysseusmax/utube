from pyrogram import filters as Filters
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


def map_btns(pos):
    if pos == 1:
        button = [[InlineKeyboardButton(text="-->", callback_data="help+2")]]
    elif pos == len(tr.HELP_MSG) - 1:
        auth = GoogleAuth(Config.CLIENT_ID, Config.CLIENT_SECRET)
        url = auth.GetAuthUrl()
        button = [
            [InlineKeyboardButton(text="<--", callback_data=f"help+{pos-1}")],
            [InlineKeyboardButton(text="Authentication URL", url=url)],
        ]
    else:
        button = [
            [
                InlineKeyboardButton(text="<--", callback_data=f"help+{pos-1}"),
                InlineKeyboardButton(text="-->", callback_data=f"help+{pos+1}"),
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
    await m.reply_chat_action("typing")
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
