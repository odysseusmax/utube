from youtube_upload.auth import GoogleAuth
from youtube_upload.youtube import Youtube

from config import Config

import os, time, traceback

class Uploader:

    def __init__(self, c, m, file, title=None):
        self.c = c
        self.m = m
        self.file = file
        self.title = title


    async def start(self, progress=None, *args):
        self.progress = progress
        self.args = args

        await self._upload()

        return self.status, self.message


    async def _upload(self):
        try:

            auth = GoogleAuth(Config.CLIENT_ID, Config.CLIENT_SECRET)

            auth.LoadCredentialsFile(Config.CRED_FILE)

            google = auth.authorize()

            properties = dict(
                title = self.title if self.title else os.path.basename(self.file),
                description = 'Uploaded to youtube with https://t.me/youtubeitbot',
                category = 27,
                privacyStatus = 'private'
            )

            youtube = Youtube(google)

            self.start_time = time.time()
            self.last_time = self.start_time

            r = await youtube.upload_video(video = self.file, properties = properties, progress = self._callback)

            self.status = True
            self.message = f"https://youtu.be/{r['id']}"
        except Exception as e:
            traceback.print_exc()
            self.status = False
            self.message = f"Error occuered during upload.\nError details: {e}"
        return

    async def _callback(self, cur, tot):
        try:
            if(self.progress):
                if(int(time.time() - self.last_time) > 6):
                    await self.progress(cur, tot, self.start_time, 'Uploading...', *self.args)
                    self.last_time = time.time()
        except Exception as e:
            print(e)
            pass

        return

