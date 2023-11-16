import os
import random
import asyncio
import logging
from typing import Optional, Tuple

from ..youtube import GoogleAuth, YouTube
from ..config import Config


log = logging.getLogger(__name__)


class Uploader:
    def __init__(self, file: str, title: Optional[str] = None):
        self.file = file
        self.title = title
        self.video_category = {
            1: "Film & Animation",
            2: "Autos & Vehicles",
            10: "Music",
            15: "Pets & Animal",
            17: "Sports",
            19: "Travel & Events",
            20: "Gaming",
            22: "People & Blogs",
            23: "Comedy",
            24: "Entertainment",
            25: "News & Politics",
            26: "Howto & Style",
            27: "Education",
            28: "Science & Technology",
            29: "Nonprofits & Activism",
        }

    async def start(self, progress: callable = None, *args) -> Tuple[bool, str]:
        self.progress = progress
        self.args = args

        await self._upload()

        return self.status, self.message

    async def _upload(self) -> None:
        try:
            loop = asyncio.get_running_loop()

            auth = GoogleAuth(Config.CLIENT_ID, Config.CLIENT_SECRET)

            if not os.path.isfile(Config.CRED_FILE):
                log.debug(f"{Config.CRED_FILE} does not exist")
                self.status = False
                self.message = "Upload failed because you did not authenticate me."
                return

            auth.LoadCredentialsFile(Config.CRED_FILE)
            google = await loop.run_in_executor(None, auth.authorize)
            if Config.VIDEO_CATEGORY and Config.VIDEO_CATEGORY in self.video_category:
                categoryId = Config.VIDEO_CATEGORY
            else:
                categoryId = random.choice(list(self.video_category))

            categoryName = self.video_category[categoryId]
            title = self.title if self.title else os.path.basename(self.file)
            title = (
                (Config.VIDEO_TITLE_PREFIX + title + Config.VIDEO_TITLE_SUFFIX)
                .replace("<", "")
                .replace(">", "")[:100]
            )
            description = (
                Config.VIDEO_DESCRIPTION
                + "\nUploaded to YouTube with https://tx.me/youtubeitbot"
            )[:5000]
            if not Config.UPLOAD_MODE:
                privacyStatus = "private"
            else:
                privacyStatus = Config.UPLOAD_MODE

            properties = dict(
                title=title,
                description=description,
                category=categoryId,
                privacyStatus=privacyStatus,
            )

            log.debug(f"payload for {self.file} : {properties}")

            youtube = YouTube(google)
            r = await loop.run_in_executor(
                None, youtube.upload_video, self.file, properties
            )

            log.debug(r)

            video_id = r["id"]
            self.status = True
            self.message = (
                f"[{title}](https://youtu.be/{video_id}) uploaded to YouTube under category "
                f"{categoryId} ({categoryName})"
            )
        except Exception as e:
            log.error(e, exc_info=True)
            self.status = False
            self.message = f"Error occuered during upload.\nError details: {e}"
