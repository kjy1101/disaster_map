from rest_framework_gis import serializers
from rest_framework import serializers as rest_serializer

from .models import Mark, Tweet

region = ["서울", "경기", "강원", "충북", "충남", "전북", "전라", "경북", "경남", "부산", "인천", "대구", "울산", "광주", "대전", "세종", "창원", "제주", "양구",
          "수원", "고양", "용인", "상남", "부천", "화성", "남양주", "안산", "안양", "평택", "원주", "춘천", "강릉", "속초", "청주", "충주", "천안", "아산", "포항",
          "구미", "전주", "익산", "창원", "김헤", "양산", "여수", "순천", "서귀포", "양산", "진주", "거제"]

# def location_created_init(attrs):
#     location = Mark.objects.create(name=)
#
# def disaster_tag_created_init(attrs):


class TweetSerializer(serializers.ModelSerializer):
    disaster_tag = rest_serializer.SerializerMethodField()

    class Meta:
        model = Tweet
        fields = ("time", "text", "user", "disaster_tag")

    def get_disaster_tag(self, obj):
        return obj.disaster_tag.name


class MarkSerializer(serializers.GeoFeatureModelSerializer):
    # tweet = TweetSerializer(many=True, source="tweet_set")
    # time = serializers.SerializerMethodField()
    # user = serializers.SerializerMethodField()
    tweet = rest_serializer.SerializerMethodField()

    def get_tweet(self, obj):
        tweets = obj.tweet_set.all().order_by('-time')
        check = obj.tweet_set.exists()
        if check:
            return TweetSerializer(instance=tweets, many=True, context=self.context).data
        else:
            tweet = Tweet.objects.create(time="default", text="default", twid="default", user="default", location=obj,
                                        disaster_tag_id=1)
            return TweetSerializer(instance=tweet, context=self.context).data

    #
    # def get_time(self, obj):
    #     if obj.tweet_set.filter(location=obj) is not None:
    #         return obj.tweet_set.filter(location=obj)[0].time
    #     return None
    #
    # def get_user(self, obj):
    #     if obj.tweet_set.filter(location=obj) is not None:
    #         return obj.tweet_set.filter(location=obj)[0].user
    #     return None
    #
    # def get_tweet(self, obj):
    #     if obj.tweet_set.filter(location=obj) is not None:
    #         return obj.tweet_set.filter(location=obj)[0].tweet
    #     return None

    class Meta:
        fields = ("id", "region_name", "tweet")
        geo_field = "location"
        model = Mark



