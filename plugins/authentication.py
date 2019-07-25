from pyrogram import Client, Filters

import traceback

from youtube_upload.auth import GoogleAuth

from config import Config

from translations import Messages as tr


@Client.on_message(Filters.private & Filters.incoming & Filters.command(['authorise']) & Filters.user(Config.AUTH_USERS))
async def _auth(c, m):

    if(len(m.command) == 1):
        await m.reply_text(text = tr.NO_AUTH_CODE_MSG)
        return

    code = m.command[1]

    try:

        auth = GoogleAuth(Config.CLIENT_ID, Config.CLIENT_SECRET)

        auth.Auth(code)

        auth.SaveCredentialsFile(Config.CRED_FILE)

        await m.reply_text(text = tr.AUTH_SUCCESS_MSG)

    except Exception as e:
        traceback.print_exc()
        await m.reply_text(text = tr.AUTH_FAILED_MSG.format(e))
