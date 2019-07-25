from pyrogram import Client, Filters

from translations import Messages as tr

from config import Config


@Client.on_message(Filters.private & Filters.incoming & Filters.command(['start']) & Filters.user(Config.AUTH_USERS))
async def _start(c, m):

    await c.send_chat_action(chat_id = m.chat.id,
        action = "typing"
    )
    await c.send_message(chat_id = m.chat.id,
        text = tr.START_MSG.format(m.from_user.first_name),
        parse_mode = "markdown",
        disable_notification = True,
        reply_to_message_id = m.message_id
    )
