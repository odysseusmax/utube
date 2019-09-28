import time, traceback

class Downloader:

    def __init__(self, c, m):
        self.c = c
        self.m = m


    async def start(self, progress=None, *args):
        self.callback = progress
        self.args = args

        await self._download()

        return self.status, self.message


    async def _download(self):
        try:
            self.start_time = time.time()
            self.last_time = self.start_time
            self.file = await self.m.reply_to_message.download(progress = self._callback)

            if(not self.file):
                self.status = False
                self.message = "Download failed!"
            else:
                self.status = True
                self.message = self.file

        except Exception as e:
            traceback.print_exc()
            self.status = False
            self.message = f"Error occuered during download.\nError details: {e}"

        return


    async def _callback(self, cur, tot):
        try:
            if(not self.callback):
                return
            if(int(time.time()-self.last_time) > 6):
                await self.callback(cur, tot, self.start_time, "Downloading...", *self.args)
                self.last_time = time.time()

        except:
            pass

        return
