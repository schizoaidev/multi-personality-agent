from dotenv import load_dotenv
load_dotenv()
from ai import get_ai_response
from twitter import send_tweet
import time

while (True):
    send_tweet(get_ai_response())
    time.sleep(300)
