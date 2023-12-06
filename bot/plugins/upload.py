import os
import time
import string
import random
import logging
import asyncio
import datetime
from typing import Tuple, Union
from pyrogram import enums

from pyrogram import StopTransmission
from pyrogram import filters as Filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

from ..translations import Messages as tr
from ..helpers.downloader import Downloader
from ..helpers.uploader import Uploader
from ..config import Config
from ..utubebot import UtubeBot
from ..youtube import GoogleAuth

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
    & Filters.command("upload")
    & Filters.user(Config.AUTH_USERS)
)
async def _upload(c: UtubeBot, m: Message):
    auth = GoogleAuth(Config.CLIENT_ID, Config.CLIENT_SECRET)
    url = auth.GetAuthUrl()
    if not os.path.exists(Config.CRED_FILE(m.chat.id)):
        await c.send_chat_action(m.chat.id, enums.ChatAction.TYPING)
        await m.reply_text(text=tr.NOT_AUTHENTICATED_MSG,

                           quote=True,
                           disable_web_page_preview=True,
                           reply_markup=InlineKeyboardMarkup(
                               [
                                   [
                                       InlineKeyboardButton(
                                           text="🌎SIGN UP🌎", url=url
                                       )
                                   ],
                                   [
                                       InlineKeyboardButton(
                                           "Help Book📚",
                                           callback_data="help+1",
                                       )
                                   ]
                               ]
                           )
                           )
        return

    if not m.reply_to_message:
        await c.send_chat_action(m.chat.id, enums.ChatAction.TYPING)
        await m.reply_text(tr.NOT_A_REPLY_MSG, True)
        return

    message = m.reply_to_message

    if not message.media:
        await c.send_chat_action(m.chat.id, enums.ChatAction.TYPING)
        await m.reply_text(tr.NOT_A_MEDIA_MSG, True)
        return

    if not valid_media(message):
        await c.send_chat_action(m.chat.id, enums.ChatAction.TYPING)
        await m.reply_text(tr.NOT_A_VALID_MEDIA_MSG, True)
        return

    if c.counter >= 6:
        await c.send_chat_action(m.chat.id, enums.ChatAction.TYPING)
        await m.reply_text(tr.DAILY_QOUTA_REACHED, True)

    snt = await m.reply_text(tr.PROCESSING, True)
    c.counter += 1
    download_id = get_download_id(c.download_controller)
    c.download_controller[download_id] = True

    download = Downloader(m)
    status, file = await download.start(progress, snt, c, download_id)
    log.debug(status, file)
    c.download_controller.pop(download_id)

    if not status:
        c.counter -= 1
        c.counter = max(0, c.counter)
        await c.send_chat_action(m.chat.id, enums.ChatAction.TYPING)
        await snt.edit_text(text=file, parse_mode=enums.ParseMode.DEFAULT)
        return

    try:

        await c.send_chat_action(m.chat.id, enums.ChatAction.UPLOAD_VIDEO)
        await snt.edit_text("Downloaded to local, Now starting to upload to youtube...")
    except Exception as e:
        log.warning(e, exc_info=True)
        pass

    title = " ".join(m.command[1:])
    user_id = m.chat.id
    upload = Uploader(file, user_id, title)
    status, file = await upload.start(progress, snt)
    log.debug(status, file)
    if not status:
        c.counter -= 1
        c.counter = max(0, c.counter)
    await c.send_chat_action(m.chat.id, enums.ChatAction.TYPING)
    await snt.edit_text(text=file, parse_mode=enums.ParseMode.DEFAULT)


def get_download_id(storage: dict) -> str:
    while True:
        download_id = "".join(
            [random.choice(string.ascii_letters) for i in range(3)])
        if download_id not in storage:
            break
    return download_id


def valid_media(media: Message) -> bool:
    if media.video:
        return True
    elif media.video_note:
        return True
    elif media.animation:
        return True
    elif media.document and "video" in media.document.mime_type:
        return True
    else:
        return False


def human_bytes(
    num: Union[int, float], split: bool = False
) -> Union[str, Tuple[int, str]]:
    base = 1024.0
    sufix_list = ["B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB"]
    for unit in sufix_list:
        if abs(num) < base:
            if split:
                return round(num, 2), unit
            return f"{round(num, 2)} {unit}"
        num /= base


async def progress(
    cur: Union[int, float],
    tot: Union[int, float],
    start_time: float,
    status: str,
    snt: Message,
    c: UtubeBot,
    download_id: str,
):
    if not c.download_controller.get(download_id):
        raise StopTransmission

    try:
        diff = int(time.time() - start_time)

        if (int(time.time()) % 5 == 0) or (cur == tot):
            await asyncio.sleep(1)
            progress_percentage = (cur / tot) * 100
            uploaded_bar = "🟢 " * int(progress_percentage / 10)
            not_uploaded_bar = "⚪ " * int((100 - progress_percentage) / 10)
            speed, unit = human_bytes(cur / diff, True)
            curr = human_bytes(cur)
            tott = human_bytes(tot)
            eta = datetime.timedelta(seconds=int(
                ((tot - cur) / (1024 * 1024)) / speed))
            elapsed = datetime.timedelta(seconds=diff)

            # Build the progress bars
            progress_bars = uploaded_bar + not_uploaded_bar

            text = (
                f"{status}\n {progress_bars} \n\n Progress: **{progress_percentage:.2f}%**\n"
                f"{curr} of {tott}\nSpeed: {speed} {unit}PS\nETA: {eta}\nElapsed: {elapsed}"
            )

            await snt.edit_text(
                text=text,
                reply_markup=InlineKeyboardMarkup(
                    [[InlineKeyboardButton("Cancel!🚫", f"cncl+{download_id}")]]
                ),
            )

    except Exception as e:
        log.info(e)
        passF
