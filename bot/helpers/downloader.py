import time
import traceback

class Downloader:

    def __init__(self, m):
        self.m = m


    def start(self, progress=None, *args):
        self.callback = progress
        self.args = args

        self._download()

        return self.status, self.message


    def _download(self):
        try:
            self.start_time = time.time()
            
            self.downloaded_file = self.m.reply_to_message.download(progress = self._callback)

            if not self.downloaded_file:
                self.status = False
                self.message = "Download failed either because user cancelled or telegram refused!"
            else:
                self.status = True
                self.message = self.downloaded_file

        except Exception as e:
            traceback.print_exc()
            self.status = False
            self.message = f"Error occuered during download.\nError details: {e}"


    def _callback(self, cur, tot):
        if not self.callback:
            return
            
        self.callback(cur, tot, self.start_time, "Downloading...", *self.args)
