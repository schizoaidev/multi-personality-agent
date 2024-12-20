from ai import get_ai_response
from twitter import send_tweet
import time
from dotenv import load_dotenv
load_dotenv()

while (True):
    send_tweet(get_ai_response())
    time.sleep(300)
