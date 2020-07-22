import os
import time
import datetime

from pyrogram import Filters

from ..translations import Messages as tr
from ..helpers.downloader import Downloader
from ..helpers.uploader import Uploader
from ..config import Config
from ..utubebot import UtubeBot


@UtubeBot.on_message(
    Filters.private 
    & Filters.incoming 
    & Filters.command('upload') 
    & Filters.user(Config.AUTH_USERS)
)
def _upload(c, m):
    if not os.path.exists(Config.CRED_FILE):
        m.reply_text(tr.NOT_AUTHENTICATED_MSG, True)
        return

    if not m.reply_to_message:
        m.reply_text(tr.NOT_A_REPLY_MSG, True)
        return

    message = m.reply_to_message

    if not message.media:
        m.reply_text(tr.NOT_A_MEDIA_MSG, True)
        return

    if not valid_media(message):
        m.reply_text(tr.NOT_A_VALID_MEDIA_MSG, True)
        return

    snt = m.reply_text(tr.PROCESSING, True)

    download = Downloader(m)

    status, file = download.start(progress, snt)

    if not status:
        snt.edit_text(text = file, parse_mode='markdown')
        return

    title = ' '.join(m.command[1:])

    upload = Uploader(file, title)

    status, link = upload.start(progress, snt)

    snt.edit_text(text = link, parse_mode='markdown')


def valid_media(media):
    if media.video:
        return True
    elif media.video_note:
        return True
    elif media.animation:
        return True
    elif media.document and 'video' in media.document.mime_type:
        return True
    else:
        return False


def human_bytes(num, split=False):
    base = 1024.0
    sufix_list = ['B','KB','MB','GB','TB','PB','EB','ZB', 'YB']
    for unit in sufix_list:
        if abs(num) < base:
            if split:
                return round(num, 2), unit
            return f"{round(num, 2)} {unit}"
        num /= base


def progress(cur, tot, start_time, status, snt):
    try:
        diff = int(time.time()-start_time)
        
        if time.time() % 5 == 0:
            time.sleep(1)
            speed, unit = human_bytes(cur/diff, True)
            curr = human_bytes(cur)
            tott = human_bytes(tot)
            eta = datetime.timedelta(seconds=int(((tot-cur)/(1024*1024))/speed))
            elapsed = datetime.timedelta(seconds=diff)
            progress = round((cur * 100) / tot, 2)
            text = f"{status}\n\n{progress}% done.\n{curr} of {tott}\nSpeed: {speed} {unit}PS\nETA: {eta}\nElapsed: {elapsed}"
            snt.edit_text(text = text)

    except Exception as e:
        print(e)
        pass
