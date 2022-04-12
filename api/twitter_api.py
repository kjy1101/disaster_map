# mac (secret key)
# from disaster_map.settings import *

# window (secret key)
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

twitter_consumer_key = env('twitter_consumer_key')
twitter_consumer_secret = env('twitter_consumer_secret')
twitter_access_token = env('twitter_access_token')
twitter_access_secret = env('twitter_access_secret')

twitter_api = twitter.Api(consumer_key=twitter_consumer_key,
                          consumer_secret=twitter_consumer_secret, 
                          access_token_key=twitter_access_token, 
                          access_token_secret=twitter_access_secret)


# 자연재해마다 사용할 검색 키워드 queries에 모두 리스트로 저장해서 넘김
# ex. queries= ["지진", "earthquake", "진동", "흔들렸"]
# 1시간에 한번씩 호출됨
def search_tweets(queries, sids=None):

    twids = [] # id_str (아이디)
    times = [] # created_at (생성시간)
    texts = [] # text (텍스트)
    users = [] # user name (유저 이름)

    stream = twitter_api.GetStreamFilter(track=queries)

    delay = 60 * 1 # 60 seconds * 60 minutes
    close_time = time.time() + delay
    # 1시간동안 트윗 데이터 모으기
    #while True:
    for tweets in stream:
        print(tweets['text'])
        print('----------------------------------')
        times.append(tweets['created_at'])
        texts.append(tweets['text'])
        twids.append(tweets['id_str'])
        users.append(tweets['user']['name'])
            # print(texts)
        #print(time.time(), close_time)
        if time.time() > close_time:
            break
        
    # 1시간동안 트윗 데이터 모은 후 모두 반환
    print("out")
    return twids, times, texts, users#, sids_new


# query = ["산불", "지진", "태풍", "홍수", "가뭄", "자연재해", "화산", "화재"]
query = ["지성"]
search_tweets(query)