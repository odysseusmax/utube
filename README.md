# [Youtube Uploader Bot](https://t.me/youtubeitbot)




> Simple [Telegram Bot](https://core.telegram.org/bots "Telegram Bots") to Upload videos to [Youtube](https://youtube.com "Youtube") written in Python3.


### Contents

* [Info](https://github.com/odysseusmax/utube#info)
* [Libraries Used](https://github.com/odysseusmax/utube#libraries-used)
* [Setup](https://github.com/odysseusmax/utube#setup)
* [Status](https://github.com/odysseusmax/utube#status)
* [Special Notes](https://github.com/odysseusmax/utube#special-notes)
* [Screenshots](https://github.com/odysseusmax/utube#screenshots)
* [Video Tutorial](https://github.com/odysseusmax/utube#video-tutorial)
* [Contact](https://github.com/odysseusmax/utube#contact)

### Info

This is a simple hobby project which i was really curious about to impliment. This is a Telegram bot which uses [Youtube Data API v3](https://developers.google.com/youtube/v3/ "Youtube Data API v3") to upload videos to Youtube. This bot uses [OAuth 2.0](https://en.wikipedia.org/wiki/OAuth#OAuth_2.0 "OAuth 2,0") to connect to your Youtube Channel.

### Libraries Used

<details>
           <summary>Pyrogram</summary>
           <p><a href="https://github.com/pyrogram/pyrogram">Pyrogram</a> is used to connect the bot with telegram servers.</p>
</details>
<details>
           <summary>Google Client API</summary>
           <p><a href="https://github.com/googleapis/google-api-python-client">Google Client API</a> is used to connect the bot with Google and then with Youtube.</p>
</details>

### Setup

:heavy_exclamation_mark: This project requires [Python3.7](https://www.python.org/downloads/release/python-370 "Python3.7") (as this was written and tested with Python 3.7.3, try and see if it works with other versions)

**Clone and setup virtual environment**

``` bash
$ git clone https://github.com/odysseusmax/utube.git

$ cd utube

$ virtualenv venv

$ source venv/bin/activate

```

**Setup config.py**

* Head to [Manage Apps](https://my.telegram.org) and get your `API_ID` and `API_HASH`, and save it at the respective positions in `config.py`

* Head to [Google console](https://console.developers.google.com "Google console"), create a new project named `Youtube Uploader` and enable `API'S AND SERVISES`. Search for `YOUTUBE DATA API v3` and enable the API. Go to [Credentials](https://console.developers.google.com/apis/credentials "Credentials") page, select your project `Youtube Uploader` create a new credential with `other` as type. Copy the `CLIENT_ID` and `CLIENT_SECRET` and paste them to `config.py`

* Head to [Bot Father](https://t.me/BotFather "Bot FAther"), create new bot and paste the bot token to `BOT_TOKEN`

* Paste the bot owner's Telegram id to `BOT_OWNER` and add `AUTH_USERS` if you need others to use your bot.

* _All the contents of `config.py` must be kept secret as they contain sensitive informations_

**Install requirements**

With all the above procedures done, its time to install our dependencies.
Run :
```bash
$ pip3 install -r requirements.txt
```

**Run bot**

Lets run our bot for the first time!
```bash
$ python3 bot.py
```
If you did everything correctly, the bot should be running. Go do `/start` to see if the bot is live or not. Follow the instructions provided by bot to setup authorisation and to start uploading.


**Or the easy way of directly deploying to heroku**

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/odysseusmax/utube/tree/master)



### Status

This project is actively maintained and will continue so until I'm tired of it.

### Special notes

* With the Youtube Data API you are awarded with 10,000 points of requests. For one video upload it costs 1605 points, regardless of file size, which calculates to about 6 uploads daily. Once you have exhausted your daily points, you have to wait till daily reset. Resets happens at 0:00 PST, i.e. 12:30 IST. So make your uploads count.

* Uploading copyright contents will leads to immediate blocking of the video, and will not be added to your `MyVideos` section of youtube. But still the video can be played directly through the link provided by the bot.

* All the videos are uploaded as private. You may change it after youtube processes the video.

### Screenshots
<p align="center">

<img  width="25%" height="25%" src="https://github.com/odysseusmax/utube/blob/master/ss/overview.jpg">

<img  width="25%" height="25%" src="https://github.com/odysseusmax/utube/blob/master/ss/bot-start.jpg">

<img  width="25%" height="25%" src="https://github.com/odysseusmax/utube/blob/master/ss/bot-help.jpg">

<img  width="25%" height="25%" src="https://github.com/odysseusmax/utube/blob/master/ss/bot-authorise.jpg">

<img  width="25%" height="25%" alt="Upload" src="https://github.com/odysseusmax/utube/blob/master/ss/bot-upload.jpg">

</p>

### Video Tutorial

<p align="center">
           <a href="http://www.youtube.com/watch?feature=player_embedded&v=LSs8b5dMWIA" target="_blank">
                      <img src="http://img.youtube.com/vi/LSs8b5dMWIA/hqdefault.jpg" alt="How To Make Telegram Bot For YouTube Videos Uploading" />
           </a>
</p>
<p align="center">
           <b>Video Tutorial</b>
</p>

### Contact

Share the FeedBack and Suggestions with me.
You can contact me [Here](https://telegram.dog/odysseusmax "Contact me")
