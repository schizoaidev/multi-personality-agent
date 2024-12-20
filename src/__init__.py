from dotenv import load_dotenv
load_dotenv()
from ai import get_ai_response
from twitter import send_tweet
import time
import random

while (True):
    send_tweet(get_ai_response())
    time.sleep(random.randint(120, 600))
