import time
import logging


log = logging.getLogger(__name__)


class Downloader:

    def __init__(self, m):
        self.m = m
        self.status = None
        self.callback = None
        self.args = None
        self.message = None
        self.start_time = None
        self.downloaded_file = None


    async def start(self, progress=None, *args):
        self.callback = progress
        self.args = args

        await self._download()

        return self.status, self.message


    async def _download(self):
        try:
            self.start_time = time.time()
            
            self.downloaded_file = await self.m.reply_to_message.download(progress = self._callback)
            
            log.debug(self.downloaded_file)

            if not self.downloaded_file:
                self.status = False
                self.message = "Download failed either because user cancelled or telegram refused!"
            else:
                self.status = True
                self.message = self.downloaded_file

        except Exception as e:
            log.error(e, exc_info=True)
            self.status = False
            self.message = f"Error occuered during download.\nError details: {e}"


    async def _callback(self, cur, tot):
        if not self.callback:
            return
            
        await self.callback(cur, tot, self.start_time, "Downloading...", *self.args)
