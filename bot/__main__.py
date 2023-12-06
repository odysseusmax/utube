import logging
from flask import Flask
from .utubebot import UtubeBot
from .config import Config
import multiprocessing

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello, this is a fake Flask route!'


def run_flask_app():
    app.run(host='0.0.0.0', port=5001, debug=Config.DEBUG)


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG if Config.DEBUG else logging.INFO)
    logging.getLogger("pyrogram").setLevel(
        logging.INFO if Config.DEBUG else logging.WARNING
    )

    # Create a process for Flask app
    flask_process = multiprocessing.Process(target=run_flask_app)

    try:
        # Start the Flask process
        flask_process.start()

        # Run your bot
        UtubeBot().run()

    finally:
        # Ensure that the Flask process is terminated when the bot finishes
        flask_process.terminate()
        flask_process.join()
