from pyrogram import Client, Filters, InlineKeyboardMarkup, InlineKeyboardButton, Emoji

from youtube_upload.auth import GoogleAuth

from config import Config

from translations import Messages as tr


@Client.on_message(Filters.private & Filters.incoming & Filters.command(['help']) & Filters.user(Config.AUTH_USERS))
async def _help(c, m):

    await c.send_chat_action(chat_id = m.chat.id,
        action = "typing"
    )
    await c.send_message(chat_id = m.chat.id,
        text = tr.HELP_MSG[1],
        parse_mode = "markdown",
        disable_notification = True,
        reply_markup = InlineKeyboardMarkup(map(1)),
        reply_to_message_id = m.message_id
    )

help_callback_filter = Filters.create(lambda _, query: query.data.startswith('help+'))
cmsg = [
    'hi',
    'Hi there!',
    f"You're Good {Emoji.SMILING_FACE_WITH_SMILING_EYES}",
    f"You're awesome {Emoji.GRINNING_FACE_WITH_BIG_EYES}",
    f"Oh You're amazing {Emoji.SMILING_FACE_WITH_HEART_EYES}",
    f"You're cool {Emoji.SMILING_FACE_WITH_SUNGLASSES}"
]

@Client.on_callback_query(help_callback_filter)
async def help_answer(c, callback_query):
    chat_id = callback_query.from_user.id
    message_id = callback_query.message.message_id
    msg = int(callback_query.data.split('+')[1])
    await c.answer_callback_query(callback_query_id = callback_query.id, text = cmsg[msg])
    await c.edit_message_text(chat_id = chat_id,    message_id = message_id,
        text = tr.HELP_MSG[msg],    reply_markup = InlineKeyboardMarkup(map(msg))
    )


def map(pos):
    if(pos==1):
        button = [
            [InlineKeyboardButton(text = '-->', callback_data = "help+2")]
        ]
    elif(pos==len(tr.HELP_MSG)-1):

        auth = GoogleAuth(Config.CLIENT_ID, Config.CLIENT_SECRET)

        url = auth.GetAuthUrl()

        button = [
            [InlineKeyboardButton(text = '<--', callback_data = f"help+{pos-1}")],
            [InlineKeyboardButton(text = 'Authentication URL', url = url)]

        ]
    else:
        button = [
            [
                InlineKeyboardButton(text = '<--', callback_data = f"help+{pos-1}"),
                InlineKeyboardButton(text = '-->', callback_data = f"help+{pos+1}")
            ],
        ]
    return button
