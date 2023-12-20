import random
from constants import *
import json

class CreateTweetHelper:

    def __init__(self, debug_flag=True):
        self.debug=debug_flag
        self.curr_tweets_count = 0
        with open(TWEETS_JSON, 'r') as file:
            self.tweets = json.load(file)
        self.maxx_tweets_count = len(self.tweets)

    def get_random_text(self, size):
        alphabet = "abcdefghijklmnopqrstuvwxyz0123456789"
        random_text = []
        for i in range(size):
            random_number = random.randint(0, 35)
            random_text.append(alphabet[random_number])
        random_text = ''.join(random_text)
        if self.debug == True:
            print(random_text)
        return random_text

    def process_tweet(self, tweet):
        idx = tweet[TEXT].find('#')
        if idx != -1:
            tweet = tweet[TEXT][:idx] + '\n\n' + tweet[TEXT][idx:]
        return tweet

    def generate_tweet(self):
        # tweet = get_random_text(50)
        tweet = self.process_tweet(self.tweets[self.curr_tweets_count % self.maxx_tweets_count])
        self.curr_tweets_count += 1
        if self.debug == True:
            print(tweet)
        return tweet