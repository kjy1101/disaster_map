from django.views.generic.base import TemplateView
from rest_framework import viewsets
from rest_framework_gis import filters

from .models import Mark
from .serializers import MarkSerializer

from rest_framework.views import APIView
from .main import tweet_main

import json
from django.shortcuts import render
from django.contrib.gis.geos import Polygon

class MapView(TemplateView):
    template_name = "map.html"


class MarkViewSet(viewsets.ReadOnlyModelViewSet):
    """Marker view set."""

    bbox_filter_field = "location"
    filter_backends = (filters.InBBoxFilter,)
    queryset = Mark.objects.all()
    serializer_class = MarkSerializer


class TweetView(APIView):
    def get(self, request):
        tweet_main()

class BoundarySet(APIView):
    def get(self, request):
        file_path = r"./TL_SCCO_CTPRVN.json"

        with open(file_path, 'r', encoding="UTF8") as file:
            data = json.load(file)
            for i in range(17):
                print(i, " - ", data["features"][i]["properties"]["CTP_KOR_NM"])
                poly = Polygon(data["features"][i]["geometry"]["coordinates"][0])
                markk = Mark(
                    name = data["features"][i]["properties"]["CTP_KOR_NM"],
                    location=poly
                )
                markk.save()
            """print(data["features"][0]["properties"]["CTP_KOR_NM"])
            print(data["features"][0]["geometry"]["coordinates"][0])
            poly = Polygon(data["features"][0]["geometry"]["coordinates"][0])
            # poly = Polygon( [[126.98032377384108, 37.55753610745512], [126.9672775091964, 37.53412613508309], [127.00641630313044, 37.54283768127655], [127.00916288516939, 37.56134633736372], [126.98032377384108, 37.55753610745512]] )
            # poly = Polygon( ((126.98032377384108, 37.55753610745512), (126.9672775091964, 37.53412613508309), (127.00641630313044, 37.54283768127655), (127.00916288516939, 37.56134633736372), (126.98032377384108, 37.55753610745512)) )
            markk = Mark(
                name = data["features"][0]["properties"]["CTP_KOR_NM"],
                location=poly
                #location = "SRID=4326;POLYGON ((126.98032377384108 37.55753610745512, 126.9672775091964 37.53412613508309, 127.00641630313044 37.54283768127655, 127.00916288516939 37.56134633736372, 126.98032377384108 37.55753610745512))"
                #location = data["features"][i]["geometry"]["coordinates"][0]
            )
            markk.save()"""
            print("file open success")

        return render(request, 'index.html')