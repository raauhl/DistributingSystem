import threading
import time
from createtweethelper import CreateTweetHelper

interval_sec_prod = 2160
interval_sec_test = 5

class CreateTweetService:

    def __init__(self):
        self.createTweetHelper = CreateTweetHelper()

    # worker to post tweets
    def background_task(self, client):
        # A background task to run every 36 minute.
        while True:
            client.create_tweet(text=self.createTweetHelper.generate_tweet())
            time.sleep(interval_sec_prod)

    def start(self, client):
        # Start the background task
        background_thread = threading.Thread(target=self.background_task(client))
        background_thread.start()
