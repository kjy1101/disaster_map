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

    # tweet_all = []

    twids = [] # id_str (아이디)
    times = [] # created_at (생성시간)
    texts = [] # text (텍스트)
    users = [] # user name (유저 이름)

    queryy = ["토르"]
    stream = twitter_api.GetStreamFilter(track=queries)

    #금지단어->나중에 파일로
    search = '오프'

    delay = 60 * 1 # 60 seconds * 1 minutes
    close_time = time.time() + delay

    # 1분동안 트윗 데이터 모으기
    for tweets in stream:
        print(tweets['text'])
        print('----------------------------------')
        if removeRT(tweets['text']):
            times.append(utc2kst(tweets['created_at']))
            texts.append(tweets['text'])
            twids.append(tweets['id_str'])
            users.append(tweets['user']['name'])

        #금지단어 제외시키기
        texts = [word.strip(search) for word in texts]
        # print(texts)

        if time.time() > close_time:
            break
        
    # 1분동안 트윗 데이터 모은 후 모두 반환
    print("out")
    return twids, times, texts, users


# query = ["산불", "지진", "태풍", "홍수", "가뭄", "자연재해", "화산", "화재"]
# search_tweets(query)

# 중복 트윗 삭제
def remove_duplicates(twids, times, texts, users):
    twids_drop_dup = []
    times_drop_dup = []
    texts_drop_dup = []
    users_drop_dup = []

    for tw,ti,te,us in zip(twids,times,texts,users):
        if tw not in twids_drop_dup:
            twids_drop_dup.append(tw)
            times_drop_dup.append(ti)
            texts_drop_dup.append(te)
            users_drop_dup.append(us)

    return twids_drop_dup,times_drop_dup,texts_drop_dup,users_drop_dup