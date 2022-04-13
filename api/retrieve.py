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
import twitter, time

# twitter api connect
twitter_consumer_key = env('twitter_consumer_key')
twitter_consumer_secret = env('twitter_consumer_secret')
twitter_access_token = env('twitter_access_token')
twitter_access_secret = env('twitter_access_secret')

twitter_api = twitter.Api(consumer_key=twitter_consumer_key,
                          consumer_secret=twitter_consumer_secret, 
                          access_token_key=twitter_access_token, 
                          access_token_secret=twitter_access_secret)

# remove RT tweets
def removeRT(text):

    if text[0] == 'R' and text[1] == 'T':
        return False
    else:
        return True

# change to korean time
def utc2kst(utc_str):
    ust = datetime.strptime(utc_str, '%a %b %d %H:%M:%S +0000 %Y')
    kst = ust + timedelta(hours=9)
    kst_str = kst.strftime('%Y.%m.%d %H:%M:%S')
    return kst_str

# 자연재해마다 사용할 검색 키워드 queries에 모두 리스트로 저장해서 넘김
# ex. queries= ["지진", "earthquake", "진동", "흔들렸"]
# 1분에 한번씩 호출됨
def search_tweets(queries):

    tweet_all = []

    stream = twitter_api.GetStreamFilter(track=queries)

    delay = 60 * 0.5 # 60 seconds * 1 minutes
    close_time = time.time() + delay

    # 1분동안 트윗 데이터 모으기
    for tweets in stream:
        # print(tweets['text'])
        # print('----------------------------------')
        tweet = {
            "time" : utc2kst(tweets['created_at']),
            "text" : tweets['text'],
            "twid" : tweets['id_str'],
            "user" : tweets['user']['name']
        }
        tweet_all.append(tweet)

        if time.time() > close_time:
            break
        
    # 1분동안 트윗 데이터 모은 후 모두 반환
    print("out")
    return tweet_all


# query = ["산불", "지진", "태풍", "홍수", "가뭄", "자연재해", "화산", "화재"]
# search_tweets(query)


def remove_duplicates(tweets):
    tweet_all=[]
    for tweet in tweets:
        if tweet['twid'] not in tweets:
            tweet_all.append(tweet)
    return tweet_all