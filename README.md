# [Youtube Uploader Bot](https://tx.me/youtubeitbot)

> Simple [Telegram Bot](https://core.telegram.org/bots "Telegram Bots") to Upload videos to [Youtube](https://youtube.com "YouTube") written in Python3.

### Contents

- [Info](#info)
- [Libraries Used](#libraries-used)
- [Setup](#setup)
- [Status](#status)
- [Special Notes](#special-notes)
- [Screenshots](#screenshots)
- [Video Tutorial](#video-tutorial)
- [Contact](#contact)
- [Commands](#commands)
- [License](#license)

## Info

#### Project Update

This is a simple hobby project which I was really curious about to implement. I [Ankit Kumar](https://github.com/alpha-alexxx/) have recently modified the code, incorporating additional functions, commands, and ensuring compatibility with the latest versions of libraries.

#### Project Overview

The project involves the development of a Telegram bot utilizing the [Youtube Data API v3](https://developers.google.com/youtube/v3/ "Youtube Data API v3"). The primary purpose of the bot is to facilitate the seamless uploading of videos to YouTube.

For more details about the original project, you can refer to the [GitHub repository](https://github.com/odysseusmax/utube).

---

_Note: The modifications made to the code aim to enhance its functionality and ensure compatibility with the most recent library versions._

### Libraries Used

- [![Pyrogram](https://img.shields.io/badge/Pyrogram-latest-green?style=flat)](https://github.com/pyrogram/pyrogram "Pyrogram")
- [![Google Client API](https://img.shields.io/badge/Google%20Client%20API-latest-blue?style=flat)](https://github.com/googleapis/google-api-python-client "Google Client API")

## Setup

**⚠️Note: This project requires Python3.6 or higher**

#### Clone and setup virtual environment

**STEP : 1** Clone the git repository with Runing :

```git
git clone https://github.com/odysseusmax/utube.git
```

**STEP : 2** Go to the repository directory.

```bash
cd utube
```

---

_Now set Environment Variables in root folder with .env file._

**STEP : 3** Create environment file to save environments.

```
cp .env.sample .env
```

Add the following lines to it, replacing `API_ID`, `API_HASH`, `BOT_TOKEN`,`CLIENT_ID`,`CLIENT_SECRET`,`BOT_OWNER`,`AUTH_USERS`,`UPLOAD_MODE` &amp; `VIDEO_CATEGORY`;

**.env File Example:**

```
BOT_TOKEN="YOUR_BOT_TOKEN_HERE"
SESSION_NAME="your_session_name_here"
API_ID="your_api_id_here"
API_HASH="your_api_hash_here"
CLIENT_ID="your_client_id_here"
CLIENT_SECRET="your_client_secret_here"
BOT_OWNER="your_bot_owner_user_id_here"
AUTH_USERS="comma_separated_list_of_user_ids"
VIDEO_DESCRIPTION="This video is uploaded from telegram bot (example)"
VIDEO_CATEGORY="your_video_category_id_here(specific if you needed)"
UPLOAD_MODE="your_upload_mode_here"
```

### Environment Variables

- `BOT_TOKEN`(Required) - Get your bot token from [Bot Father](https://tx.me/BotFather "Bot Father").
- `SESSION_NAME`(optional) - Your bot's username.
- `API_ID`(Required) - Your telegram api id, get from [Manage Apps](https://my.telegram.org).
- `API_HASH`(Required) - Your telegram api hash, get from [Manage Apps](https://my.telegram.org).
- `CLIENT_ID`(Required) - Your google client id.
- `CLIENT_SECRET`(Required) - Your google client secret.
- `BOT_OWNER`(Required) - Telegram id of bot owner.
- `AUTH_USERS`(optional) - Telegram id's of authorised users, separated by `,`.
- `VIDEO_DESCRIPTION`(optional) - Any default description to be aded to the video.
- `VIDEO_CATEGORY`(optional) - YouTube's video category id. If not specified or specified id is invalid, category id will be selected randomly.
- `VIDEO_TITLE_PREFIX`(optional) - Any prefix to be added to the video's title.
- `VIDEO_TITLE_SUFFIX`(optional) - Any suffix to be added to the video's title.
- `UPLOAD_MODE`(optional) - The video's privacy status. Valid values for this property are: `private`, `public`, `unlisted`.
- `DEBUG` (optional) - Whether to set logging level to DEBUG. If set logging will be set to DEBUG level, else INFO level.

**Getting your `CLIENT_ID` and `CLIENT_SECRET`**

Certainly! To obtain the `CLIENT_ID` and `CLIENT_SECRET` for the YouTube Data API v3 from the Google Cloud Console, you can follow these steps:

#### Step 1: Create a Project on Google Cloud Console

1.  Open the [Google Cloud Console](https://console.cloud.google.com/).
2.  Click on the project drop-down menu at the top of the page and select **[New Project](https://console.cloud.google.com/projectcreate)**.
3.  Enter a name for your project - 'Youtube Uploader' and click **Create**.

#### Step 2: Enable the YouTube Data API v3

1.  In the Google Cloud Console, navigate to the [APIs & Services Dashboard](https://console.cloud.google.com/apis/dashboard).
2.  Click on **\+ ENABLE APIS AND SERVICES**.
3.  Search for "**YouTube Data API v3**" and select it.
4.  Click **Enable**.

#### Step 3: Create Credentials

1.  In the Google Cloud Console, navigate to the [Credentials page](https://console.cloud.google.com/apis/credentials).
2.  Click **Create Credentials** and select **OAuth client ID**.
3.  Choose **Web Application** as the application type.
4.  Enter a name - `Youtube Uploader` for your OAuth client.
5.  Click **Create**.

#### Step 4: Obtain `CLIENT_ID` and `CLIENT_SECRET`

1.  After creating the OAuth client, you will see a pop-up with your `CLIENT_ID` and `CLIENT_SECRET`. It will also be available on the Credentials page under the "OAuth 2.0 Client IDs" section.
2.  Copy the `CLIENT_ID` and `CLIENT_SECRET` and store them securely.
3. Configure your application with this authorized redirect URIs `https://gogoauth.vercel.app`.

#### Step 5: Configure OAuth Consent Screen

1.  On the [Credentials page](https://console.cloud.google.com/apis/credentials), click on the **OAuth consent screen** tab.
2.  Fill in the necessary information, including the **Scopes** required for your application.
3.  Save the changes.
--------
_Now you have obtained the `CLIENT_ID` and `CLIENT_SECRET` for the YouTube Data API v3. Include these credentials in your application code securely. Make sure to follow best practices for handling API keys and secrets to keep your application secure._

-----

**Activate Python virtual Environment**
```python
python3 -m venv venv
```
**Go to Venv**
```python
source venv/bin/activate
```

**Install requirements**
```python
 pip3 install -r requirements.txt
```

**Run bot**

Lets run our bot for the first time!

```python
python3 -m bot
```

If you did everything correctly, the bot should be running. Go do `/start` to see if the bot is live or not. Follow the instructions provided by bot to setup authorisation and to start uploading.

### Deploying to Render with Ease

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://dashboard.render.com/select-repo?type=web)

#### Instructions:

1. **Public Git Repository:**
   - Add this public Git repository URL: `https://github.com/odysseusmax/utube.git`

2. **Name Your Service:**
   - Provide a name for your service.
   - In the "Advanced" tab, add a secret file named `.env` with all required environment variables.

3. **Create Web Service:**
   - Set up your web service configuration.

4. **Wait for Deployment:**
   - Monitor the deployment progress.
   - Once completed, your site will be ![Live](https://img.shields.io/badge/live-brightgreen).

5. **Configure Cron Job:**
   - Copy the deployed website URL.
   - Create an account on [CRON JOB](https://console.cron-job.org/signup) if you haven't already.
   - [Create a new cron job](https://console.cron-job.org/jobs/create), providing a title and pasting your website URL.
   - Click on **CREATE** or firstly, test run the cron job and then Create.

---

**Notes:**
1. _Your bot is now live 24/7._
2. _A cron job is set up to address Render's free service limitations, which may cause the service to stop every 15 minutes._

### Development Status
[![Active](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)](https://github.com/alpha-alexxx/YoutubeUploader)

🚀 **Active Development:** I am currently actively working on this project, implementing new features, fixing issues, and making continuous improvements. Your contributions and feedback are always welcome!

### Special notes
1. With the Youtube Data API you are awarded with 10,000 points of requests. For one video upload it costs 1605 points, regardless of file size, which calculates to about 6 uploads daily. Once you have exhausted your daily points, you have to wait till daily reset. Resets happens at 0:00 PST, i.e. 12:30 IST. So make your uploads count.
2. Uploading copyright contents will leads to immediate blocking of the video.

3. By default, all the videos are uploaded as private with random category id unless you provide `UPLOAD_MODE` and `VIDEO_CATEGORY`. You may change it after youtube processes the video.

### Commands

Edit the bot in [**BotFather**](https://t.me/BotFather) with command `/help` ⮞ `/mybots` ⮞ choose your bot by the username ⮞ click on Edit bot ⮞ click on edit commands ⮞ copy the below code and paste there and save it.

```
start -  Start the bot.
login - Log in to the bot
upload -  Initiate the upload process of video
help -  Get assistance or command information
logout - Log out from the bot
refresh -  Refresh or update auth token
```
### Example

Visit Demo [BotExample.md](BotExample.md)


### Video Tutorial

Here's a YouTube tutorial video for deploying the bot on [Heroku](https://heroku.com/ "Heroku"). [Video Link](http://www.youtube.com/watch?v=LSs8b5dMWIA "Tutorial video for deploying to Heroku").

### Contact

- Feel free to reach out to me on Telegram: [@odysseusmax](https://telegram.dog/odysseusmax).

- Join the active contributors on Telegram: [![Telegram Group](https://img.shields.io/badge/Telegram-Join%20Telegram%20Group-blue.svg?logo=telegram)](https://telegram.dog/LethargicBots)

### License

Code released under [GNU General Public License v3.0](https://opensource.org/licenses/GPL-3.0).
[![License](https://img.shields.io/badge/License-GPL%20v3.0-blue.svg)](LICENSE)
