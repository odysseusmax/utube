import os
import time
import random

import httplib2
import http
from apiclient.http import MediaFileUpload
from apiclient.errors import HttpError


class MaxRetryExceeded(Exception):
    pass
class UploadFailed(Exception):
    pass

class YouTube:

    MAX_RETRIES = 10

    RETRIABLE_EXCEPTIONS = (httplib2.HttpLib2Error, IOError,
                        http.client.NotConnected,
                        http.client.IncompleteRead,
                        http.client.ImproperConnectionState,
                        http.client.CannotSendRequest,
                        http.client.CannotSendHeader,
                        http.client.ResponseNotReady,
                        http.client.BadStatusLine)

    RETRIABLE_STATUS_CODES = [500, 502, 503, 504]

    def __init__(self, auth, chunksize=-1):
        self.youtube = auth
        self.request = None
        self.chunksize = chunksize
        self.response = None
        self.error = None
        self.retry = 0




    def upload_video(self, video, properties, progress=None, *args):
        self.progress = progress
        self.progress_args = args
        self.video = video
        self.properties = properties

        body = dict(
            snippet=dict(
                title = self.properties.get('title'),
                description = self.properties.get('description'),
                categoryId = self.properties.get('category')
            ),
            status=dict(
                privacyStatus=self.properties.get('privacyStatus')
            )
        )

        media_body = MediaFileUpload(self.video, chunksize=self.chunksize,
            resumable=True, mimetype="application/octet-stream"
        )

        self.request = self.youtube.videos().insert(part = ','.join(body.keys()), body=body, media_body=media_body)
        self._resumable_upload()
        return self.response


    def _resumable_upload(self):
        response = None
        while response is None:
            try:
                status, response = self.request.next_chunk()
                if response is not None:
                    if('id' in response):
                        self.response = response
                    else:
                        self.response = None
                        raise UploadFailed("The file upload failed with an unexpected response:{}".format(response))
            except HttpError as e:
                if e.resp.status in self.RETRIABLE_STATUS_CODES:
                    self.error = "A retriable HTTP error {} occurred:\n {}".format(e.resp.status, e.content)
                else:
                    raise
            except self.RETRIABLE_EXCEPTIONS as e:
                self.error = "A retriable error occurred: {}".format(e)

            if self.error is not None:
                print(self.error)
                self.retry += 1

                if self.retry > self.MAX_RETRIES:
                    raise MaxRetryExceeded("No longer attempting to retry.")

                max_sleep = 2 ** self.retry
                sleep_seconds = random.random() * max_sleep

                print("Sleeping {} seconds and then retrying...".format(sleep_seconds))
                time.sleep(sleep_seconds)


def print_response(response):
    for key, value in response.items():
        print(key, " : ", value, '\n\n')
