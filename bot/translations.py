class Messages:
    START_MSG = (
        "<strong class='center' >Hello there, Mr. {}! 🤖</strong>\n\n"
        "I am the Youtube Uploader Bot. My purpose is to assist you in uploading Telegram videos to YouTube 📤 \n"
        "once you grant me the necessary authorization 🔑.\n\n"
        "Directly Initiate the process <strong>/login ↫</strong>\n"
        "or You can follow the <strong>Help Book.</strong>"
    )

    HELP_MSG = [
        ".",
        "Greetings! 📚\n\n"
        "Before we begin, it's important to understand that every video you upload to YouTube is subject to YouTube's content checks. "
        "Their advanced AI can detect copyrighted content, and videos violating their guidelines may be flagged. "
        "Let's delve into how I operate.",
        "**Understanding the Process**\n\n"
        "**Step 1:** Authorize me to upload videos to your YouTube channel. We'll cover this in detail in the following pages.\n\n"
        "**Step 2:** Forward a Telegram video to me.\n\n"
        "**Step 3:** Reply with `/upload` to the forwarded video file. You can optionally provide a title in the upload command; "
        "however, it's not mandatory. If you omit the title, the filename will be used as the video title.\n\n"
        "**Step 4:** I'll remotely download the file and upload it to your YouTube channel.\n\n"
        "**Step 5:** After the upload is complete, I'll send you the YouTube link to your video.",
        "**Creating Your YouTube Channel** 📹\n\n"
        "If you don't already have a YouTube channel, it's a prerequisite for using my services. "
        "Follow these steps to create your own channel:\n\n"
        "**Step 1:** Sign in to YouTube on a computer or using the mobile app.\n\n"
        "**Step 2:** Try any action that requires a channel, such as uploading a video, posting a comment, or creating a playlist.\n\n"
        "**Step 3:** If you don't have a channel yet, you'll receive a prompt to create one.\n\n"
        "**Step 4:** Review the details and confirm to create your new channel.",
        "**Verifying Your YouTube Account** ✔️\n\n"
        "YouTube takes spam and abuse seriously. To upload videos longer than 15 minutes, "
        "you need to verify your YouTube account. If you haven't done so, "
        "videos longer than 15 minutes may be removed. You can verify your account [here](http://www.youtube.com/verify)."
        "\n\nPlease remember to verify your account to keep your uploads public. 🔐",
        "**Authorizing Your Account** 🔑\n\n"
        "To grant me access to upload videos to your YouTube account, open the provided link, "
        "**allow access, and copy the code. Return here, paste and send the code.**"
        "\n\nRest assured, I am not a hacker or privacy invader. I respect your privacy and I'm here to assist. "
        "If I were a hacker, I wouldn't be developing Telegram Bots. 💼",
    ]

    LOGIN_MSG = (
        "**__You're interested in logging in. Excellent!__**\n\n"
        "To proceed, you'll need to grant me permission to upload videos to your YouTube account. "
        "Click the button below to authorize access and copy the code provided. \n\n"
        "**Then, return here, paste and send your code📋.**"
    )

    UPGRADE_MSG = ""

    NOT_A_REPLY_MSG = "Please reply with a video file. 📽️"

    NOT_A_MEDIA_MSG = "No media file found. " + NOT_A_REPLY_MSG

    NOT_A_VALID_MEDIA_MSG = "This is not a valid media. 🚫"

    DAILY_QUOTA_REACHED = (
        "Dear user,\n\n"
        "It has come to our attention that you are currently attempting to upload more than six videos today. "
        "Please be advised that, as per YouTube's default policy, users are limited to a maximum of six uploads per day.\n\n"
        "We kindly request you to consider resuming your video uploads on the following day.\n\n"
        "Thank you for your understanding and cooperation. \n\n"
        "Best regards,\n**LethargicBots**"
    )

    PROCESSING = "Processing... ⌛"

    NOT_AUTHENTICATED_MSG = (
        "You have not authorized me to upload videos to any account.🚫\n\n"
        "Please refer the below menu to understand the process."
    )

    NO_AUTH_CODE_MSG = "No authorization code provided. Please enter a valid code.🚫"

    AUTH_SUCCESS_MSG = (
        "Congratulations! You have successfully granted me permission to upload videos to your YouTube account."
        "\n\n**Thank you 🎁 for choosing to use my services!**\n\n"
        "Happy uploading! 🎉"
    )

    AUTH_FAILED_MSG = "Authentication failed. Details: {} ❌"

    AUTH_DATA_SAVE_SUCCESS = "Authorization data successfully saved!✅"

    LOGOUT_SUCCESS_MSG = (
        "**Authorization revoked successfully. Your access has been terminated.**✅"
    )

    LOGOUT_FAILED_MSG = (
        "**Failed to revoke authorization.**❌\n\n"
        "I couldn't find credentials.json in environment.\n"
        "🤔 Did it mysteriously vanish? No worries! Here's what you can do:\n\n"
        "**1.** 🚀Initiate a session\n"
        "**OR**\n"
        "**2.** 📚Check the helpbook"
    )

    NO_CREDENTIALS_MSG = "You haven't authorize yet.🚫"
    TOKEN_REFRESH_SUCCESS_MSG = "Token refreshed successfully. Now you can upload your videos."
    TOKEN_REFRESH_NOT_FOUND_OR_NOTEXPIRED_MSG = (
        "🚨**TOKEN NOT FOUND**🚨\n\n"
        "Oops! It seems like Authorization token is missing from the environment.\n"
        "🤔 Did it mysteriously vanish? No worries! Here's what you can do:\n\n"
        "**1.** 🚪First things first, try out **Logout**.\n"
        "**2.** 🚀Initiate a session with **Login**."
    )
    TOKEN_REFRESH_FAILED_MSG = "Token is not expired or refresh token is missing."