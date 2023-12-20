import tweepy
import json
from createtweetservice import CreateTweetService
from constants import *

debug=True

# import secrets
with open(SECRETS_JSON, 'r') as file:
    data = json.load(file)

# intialize secrets
api_key = data[API_KEY]
api_key_secret = data[API_KEY_SECRET]
bearer_token = data[BEARER_TOKEN]
access_token = data[ACCESS_TOKEN]
access_token_secret = data[ACCESS_TOKEN_SECRET]

# setup tweepy
client = tweepy.Client(bearer_token, api_key, api_key_secret, access_token, access_token_secret)
auth = tweepy.OAuth1UserHandler(api_key, api_key_secret, access_token, access_token_secret)
api = tweepy.API(auth)

CreateTweetService = CreateTweetService();
CreateTweetService.start(client)