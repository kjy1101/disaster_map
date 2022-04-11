import twitter

from disaster_map.settings import *

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


query = ["석촌호수"]
stream = twitter_api.GetStreamFilter(track=query)

for tweets in stream:
    print(tweets)


