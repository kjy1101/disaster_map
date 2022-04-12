from time import time
#from twitter_api import twitter_api_api, utc2kst, removeRT
import time
from datetime import datetime
#from twitter_api import *
import twitter_api

def main(interval=60):
    """query = ["지성"]
    stream = twitter_api_api.GetStreamFilter(track=query)
    times = []

    for tweets in stream:
        print('***********crawling***********')
        if removeRT(tweets['text']):
            time = utc2kst(tweets['created_at'])
            times.append(time)
            print(tweets)"""

    while True:
        t0 = time.time()
        t_tot = time.time()-t0
        print("***")
        print(time.time())

        # 트윗 가져오기
        queries = ["산불"]
        twids,times,texts,users = twitter_api.search_tweets(queries)

        time.sleep(60) # 60초에 한번씩 실행
    
    print("out")


if __name__ == '__main__':
    main(interval=60)