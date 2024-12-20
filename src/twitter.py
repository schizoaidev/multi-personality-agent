import os
import tweepy

client = tweepy.Client(
    consumer_key=os.getenv("X_CONSUMER"),
    consumer_secret=os.getenv("X_CONSUMER_SECRET"),
    access_token=os.getenv("X_ACCESS_TOKEN"),
    access_token_secret=os.getenv("X_ACCESS_TOKEN_SECRET")
)

def send_tweet(text):
    client.create_tweet(text=text)

