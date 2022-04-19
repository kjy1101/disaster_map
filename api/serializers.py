from rest_framework_gis import serializers

from .models import Mark

region = ["서울", "경기", "강원", "충북", "충남", "전북", "전라", "경북", "경남", "부산", "인천", "대구", "울산", "광주", "대전", "세종", "창원", "제주", "양구",
          "수원", "고양", "용인", "상남", "부천", "화성", "남양주", "안산", "안양", "평택", "원주", "춘천", "강릉", "속초", "청주", "충주", "천안", "아산", "포항",
          "구미", "전주", "익산", "창원", "김헤", "양산", "여수", "순천", "서귀포", "양산", "진주", "거제"]

# def location_created_init(attrs):
#     location = Mark.objects.create(name=)
#
# def disaster_tag_created_init(attrs):

class MarkSerializer(serializers.GeoFeatureModelSerializer):

    class Meta:
        fields = ("id", "name")
        geo_field = "location"
        model = Mark