from pyrogram import Client, Filters

import time, datetime, os

from translations import Messages as tr

from helpers.downloader import Downloader

from helpers.uploader import Uploader

from config import Config


@Client.on_message(Filters.private & Filters.incoming & Filters.command(['upload']) & Filters.user(Config.AUTH_USERS))
async def _upload(c, m):
    if(not os.path.isfile(Config.CRED_FILE)):
        await m.reply_text(text = tr.NOT_AUTHENTICATED_MSG)
        return

    if(not m.reply_to_message):
        await m.reply_text(text = tr.NOT_A_REPLY_MSG)
        return

    message = m.reply_to_message

    if(not message.media):
        await m.reply_text(text = tr.NOT_A_MEDIA_MSG)
        return

    if(not valid_media(message)):
        await m.reply_text(text = tr.NOT_A_VALID_MEDIA_MSG)
        return

    snt = await c.send_message(chat_id = m.chat.id,
        text = tr.PROCESSING,
        reply_to_message_id = m.message_id
    )

    download = Downloader(c, m)

    status, file = await download.start(progress, snt)

    if(not status):
        await snt.edit_text(text = file, parse_mode='markdown')
        return

    title = ' '.join(m.command[1:])

    upload = Uploader(c, m, file, title)

    status, link = await upload.start(progress, snt)

    await snt.edit_text(text = link, parse_mode='markdown')


def valid_media(media):
    if(media.video):
        return True
    elif(media.video_note):
        return True
    elif(media.animation):
        return True
    elif(media.document and 'video' in media.document.mime_type):
        return True
    else:
        return False


async def progress(cur, tot, start_time, status, snt):
    try:
        diff = int(time.time()-start_time)

        speed = round((cur/(1024**2))/diff,2)

        curr = round(cur/(1024**2), 2)

        tott = round(tot/(1024**2), 2)

        eta = datetime.timedelta(seconds=int(((tot-cur)/(1024*1024))/speed))

        progress = round((cur * 100) / tot,2)

        text = f"**{status}**\n\n`{progress}%` done.\n**{curr}MB** of **{tott}MB**\nSpeed: **{speed}MBPS**\nETA: **{eta}**"

        await snt.edit_text(text = text)

    except Exception as e:
        print(e)
        pass
