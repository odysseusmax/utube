from typing import Optional
import httplib2
import os
import requests

from apiclient import discovery
from oauth2client.client import (
    OAuth2WebServerFlow,
    FlowExchangeError,
    OAuth2Credentials,
)
from oauth2client.file import Storage


class AuthCodeInvalidError(Exception):
    pass


class InvalidCredentials(Exception):
    pass


class NoCredentialFile(Exception):
    pass


class GoogleAuth:
    OAUTH_SCOPE = ["https://www.googleapis.com/auth/youtube.upload"]
    REDIRECT_URI = "https://gogoauth.vercel.app"
    API_SERVICE_NAME = "youtube"
    API_VERSION = "v3"

    def __init__(self, CLIENT_ID: str, CLIENT_SECRET: str):
        self.flow = OAuth2WebServerFlow(
            CLIENT_ID, CLIENT_SECRET, self.OAUTH_SCOPE, redirect_uri=self.REDIRECT_URI
        )
        self.credentials: Optional[OAuth2Credentials] = None

    def GetAuthUrl(self) -> str:
        return self.flow.step1_get_authorize_url()

    def Auth(self, code: str) -> None:
        try:
            self.credentials = self.flow.step2_exchange(code)
        except FlowExchangeError as e:
            raise AuthCodeInvalidError(e)
        except Exception:
            raise

    def authorize(self):
        try:
            if self.credentials:
                http = httplib2.Http()
                self.credentials.refresh(http)
                http = self.credentials.authorize(http)
                return discovery.build(
                    self.API_SERVICE_NAME, self.API_VERSION, http=http, cache_discovery=False
                )
            else:
                raise InvalidCredentials("No credentials!")
        except Exception:
            raise

    def LoadCredentialsFile(self, cred_file: str) -> None:
        if not os.path.isfile(cred_file):
            raise NoCredentialFile(
                "No credential file named {} is found.".format(cred_file)
            )
        storage = Storage(cred_file)
        self.credentials = storage.get()

    def SaveCredentialsFile(self, cred_file: str) -> None:
        storage = Storage(cred_file)
        storage.put(self.credentials)

    def revoke(self) -> None:
        if self.credentials:
            access_token = self.credentials.access_token
            revoke_url = f"https://accounts.google.com/o/oauth2/revoke?token={access_token}"
            response = requests.get(revoke_url)

            if response.status_code == 200:
                print("Token revoked successfully")
                self.credentials = None
            else:
                print(f"Failed to revoke token, response code: {response.status_code}")
        else:
            print("No credentials to revoke")