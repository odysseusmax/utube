from apiclient.discovery import build
from apiclient.errors import ResumableUploadError
from oauth2client.client import OAuth2WebServerFlow, FlowExchangeError
from oauth2client.file import Storage
from oauth2client import file, client, tools
import httplib2, http, os


class AuthCodeInvalidError(Exception):
    pass

class InvalidCredentials(Exception):
    pass

class NoCredentialFile(Exception):
    pass


class GoogleAuth:
    OAUTH_SCOPE = ['https://www.googleapis.com/auth/youtube.upload']
    REDIRECT_URI = "urn:ietf:wg:oauth:2.0:oob"
    API_SERVICE_NAME = 'youtube'
    API_VERSION = 'v3'


    def __init__(self, CLIENT_ID, CLIENT_SECRET):
        self.flow = OAuth2WebServerFlow(
            CLIENT_ID,
            CLIENT_SECRET,
            self.OAUTH_SCOPE,
            redirect_uri=self.REDIRECT_URI
        )
        self.credentials = None


    def GetAuthUrl(self):
        return self.flow.step1_get_authorize_url()


    def Auth(self, code):
        try:
            self.credentials = self.flow.step2_exchange(code)
        except FlowExchangeError as e:
            raise AuthCodeInvalidError(e)
        except:
            raise


    def authorize(self):
        try:
            if(self.credentials):
                http = httplib2.Http()
                self.credentials.refresh(http)
                http = self.credentials.authorize(http)
                return build(self.API_SERVICE_NAME, self.API_VERSION, http=http)
            else:
                raise InvalidCredentials('No credentials!')
        except:
            raise


    def LoadCredentialsFile(self, cred_file):
        if(not os.path.isfile(cred_file)):
            raise NoCredentialFile('No credential file named {} is found.'.format(cred_file))
        storage = Storage(cred_file)
        self.credentials = storage.get()


    def SaveCredentialsFile(self, cred_file):
        storage = Storage(cred_file)
        storage.put(self.credentials)

