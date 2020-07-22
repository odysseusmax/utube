import os
import time
import string
import random
import datetime

from pyrogram import Filters, InlineKeyboardMarkup, InlineKeyboardButton

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
    
    if c.counter >= 6:
        m.reply_text(tr.DAILY_QOUTA_REACHED, True)

    snt = m.reply_text(tr.PROCESSING, True)
    c.counter += 1
    download_id = get_download_id(c.download_controller)
    c.download_controller[download_id] = True

    download = Downloader(m)
    status, file = download.start(progress, snt, c, download_id)
    c.download_controller.pop(download_id)
    
    if not status:
        c.counter -= 1
        c.counter = max(0, c.counter)
        snt.edit_text(text = file, parse_mode='markdown')
        return
    time.sleep(5)
    snt.edit_text("Downloaded to local, Now starting to upload to youtube...")
    title = ' '.join(m.command[1:])
    upload = Uploader(file, title)
    status, link = upload.start(progress, snt)
    if not status:
        c.counter -= 1
        c.counter = max(0, c.counter)
    snt.edit_text(text = link, parse_mode='markdown')


def get_download_id(storage):
    while True:
        download_id = ''.join([random.choice(string.ascii_letters) for i in range(3)])
        if download_id not in storage:
            break
    return download_id


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


def progress(cur, tot, start_time, status, snt, c, download_id):
    if not c.download_controller.get(download_id):
        raise c.StopTransmission
        
    try:
        diff = int(time.time()-start_time)
        
        if (int(time.time()) % 5 == 0) or (cur==tot):
            time.sleep(1)
            speed, unit = human_bytes(cur/diff, True)
            curr = human_bytes(cur)
            tott = human_bytes(tot)
            eta = datetime.timedelta(seconds=int(((tot-cur)/(1024*1024))/speed))
            elapsed = datetime.timedelta(seconds=diff)
            progress = round((cur * 100) / tot, 2)
            text = f"{status}\n\n{progress}% done.\n{curr} of {tott}\nSpeed: {speed} {unit}PS\nETA: {eta}\nElapsed: {elapsed}"
            snt.edit_text(
                text = text, 
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton('Cancel!', f'cncl+{download_id}')
                        ]
                    ]
                )
            )

    except Exception as e:
        print(e)
        pass
