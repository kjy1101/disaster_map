import time
import twitter_api

def main(interval=60):

    while True:
        t0 = time.time()
        t_tot = time.time()-t0
        print("***")
        print(time.time())

        # 트윗 가져오기
        queries = ["산불"]
        twids,times,texts,users = twitter_api.search_tweets(queries)

        time.sleep(60) # 60초에 한번씩 실행


if __name__ == '__main__':
    main(interval=60)