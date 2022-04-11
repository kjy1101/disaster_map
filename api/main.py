import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "disaster_map.settings")

import django
django.setup()

from api.twitter_api import twitter_api, utc2kst


def main(interval=60):
    query = ["석촌호수"]
    stream = twitter_api.GetStreamFilter(track=query)
    times = []

    for tweets in stream:
        time = utc2kst(tweets['created_at'])
        times.append(time)
        print(tweets)