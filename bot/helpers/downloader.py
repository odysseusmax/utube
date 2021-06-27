import time
import logging
from typing import Optional, Tuple, Union

from pyrogram.types import Message


log = logging.getLogger(__name__)


class Downloader:
    def __init__(self, m: Message):
        self.m = m
        self.status: Optional[bool] = None
        self.callback: Optional[callable] = None
        self.args: Optional[tuple] = None
        self.message: Optional[str] = None
        self.start_time: Optional[float] = None
        self.downloaded_file: Optional[str] = None

    async def start(self, progress: callable = None, *args) -> Tuple[bool, str]:
        self.callback = progress
        self.args = args

        await self._download()

        return self.status, self.message

    async def _download(self) -> None:
        try:
            self.start_time = time.time()

            self.downloaded_file = await self.m.reply_to_message.download(
                progress=self._callback
            )

            log.debug(self.downloaded_file)

            if not self.downloaded_file:
                self.status = False
                self.message = (
                    "Download failed either because user cancelled or telegram refused!"
                )
            else:
                self.status = True
                self.message = self.downloaded_file

        except Exception as e:
            log.error(e, exc_info=True)
            self.status = False
            self.message = f"Error occuered during download.\nError details: {e}"

    async def _callback(self, cur: Union[int, float], tot: Union[int, float]) -> None:
        if not self.callback:
            return

        await self.callback(cur, tot, self.start_time, "Downloading...", *self.args)
