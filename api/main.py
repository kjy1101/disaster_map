from api.twitter_api import twitter_api, utc2kst, removeRT


def main(interval=60):
    query = ["지성"]
    stream = twitter_api.GetStreamFilter(track=query)
    times = []

    for tweets in stream:
        print('***********crawling***********')
        if removeRT(tweets['text']):
            time = utc2kst(tweets['created_at'])
            times.append(time)
            print(tweets)


if __name__ == '__main__':
    main(interval=60)