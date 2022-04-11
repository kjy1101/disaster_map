# mac (secret key)
# from disaster_map.settings import *

# window (secret key)
from datetime import datetime, timedelta
import time
from pathlib import Path
import os
import environ

BASE_DIR = Path(__file__).resolve().parent.parent
env = environ.Env(
    DEBUG=(bool, False)
)
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

# main code start
import twitter, json

twitter_consumer_key = env('twitter_consumer_key')
twitter_consumer_secret = env('twitter_consumer_secret')
twitter_access_token = env('twitter_access_token')
twitter_access_secret = env('twitter_access_secret')

twitter_api = twitter.Api(consumer_key=twitter_consumer_key,
                          consumer_secret=twitter_consumer_secret, 
                          access_token_key=twitter_access_token, 
                          access_token_secret=twitter_access_secret)

# account = "@SpiderManMovie"
# statuses = twitter_api.GetUserTimeline(screen_name=account, count=200, include_rts=True, exclude_replies=False)
#
# for status in statuses:
#     print(status.text)


# query = ["산불"]
# output_file_name = "stream_result.txt"
# with open(output_file_name, "w", encoding="utf-8") as output_file:
#     stream = twitter_api.GetStreamFilter(track=query)
#     while True:
#         for tweets in stream:
#             tweet = json.dumps(tweets, ensure_ascii=False)
#             print(tweet, file=output_file, flush=True)
#

# UTC->KST
# utc2kst(tweet['created_at']
def utc2kst(utc_str):
    ust = datetime.strptime(utc_str, '%a %b %d %H:%M:%S +0000 %Y')
    kst = ust + timedelta(hours=9)
    kst_str = kst.strftime('%Y.%m.%d %H:%M:%S')
    return kst_str



