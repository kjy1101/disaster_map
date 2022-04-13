import main

tweets_by_disaster = {
    "typhoon" : [],
    "downpour" : [],
    "snow" : [],
    "gale" : [],
    "drought" : [],
    "forestfire" : [],
    "earthquake" : [],
    "coldwave" : [],
    "heatwave" : [],
    "dust" : []
}

def classify_tweets(tweet_all):

    for tweet in tweet_all:
        
        if any(disaster in tweet["text"] for disaster in main.queries_typhoon):
            print("태풍 관련 트윗이다.")
            tweets_by_disaster["typhoon"].append(tweet)

        elif any(disaster in tweet["text"] for disaster in main.queries_downpour):
            print("폭우 관련 트윗이다.")
            tweets_by_disaster["downpour"].append(tweet)

        elif any(disaster in tweet["text"] for disaster in main.queries_snow):
            print("폭설 관련 트윗이다.")
            tweets_by_disaster["snow"].append(tweet)

        elif any(disaster in tweet["text"] for disaster in main.queries_gale):
            print("강풍 관련 트윗이다.")
            tweets_by_disaster["gale"].append(tweet)

        elif any(disaster in tweet["text"] for disaster in main.queries_drought):
            print("가뭄 관련 트윗이다.")
            tweets_by_disaster["drought"].append(tweet)
        
        elif any(disaster in tweet["text"] for disaster in main.queries_forestfire):
            print("산불 관련 트윗이다.")
            tweets_by_disaster["forestfire"].append(tweet)

        elif any(disaster in tweet["text"] for disaster in main.queries_earthquake):
            print("지진 관련 트윗이다.")
            tweets_by_disaster["earthquake"].append(tweet)

        elif any(disaster in tweet["text"] for disaster in main.queries_coldwave):
            print("한파 관련 트윗이다.")
            tweets_by_disaster["coldwave"].append(tweet)

        elif any(disaster in tweet["text"] for disaster in main.queries_heatwave):
            print("폭염 관련 트윗이다.")
            tweets_by_disaster["heatwave"].append(tweet)

        elif any(disaster in tweet["text"] for disaster in main.queries_dust):
            print("미세먼지 관련 트윗이다.")
            tweets_by_disaster["dust"].append(tweet)

        else:
            print("무관한 트윗이다.")

    return tweets_by_disaster