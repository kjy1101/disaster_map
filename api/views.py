from django.views.generic.base import TemplateView
from rest_framework import viewsets
from rest_framework_gis import filters

from .models import Mark
from .serializers import MarkSerializer

from rest_framework.views import APIView
from .main import tweet_main

import json
from django.shortcuts import render

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
                print(i, " - ", data["features"][i]["properties"]["CTP_KOR_NM"], " : ", data["features"][i]["geometry"]["coordinates"][0][0])
                """markk = Mark(
                    name = data["features"][i]["properties"]["CTP_KOR_NM"],
                    #location = data["features"][i]["geometry"]["coordinates"][0]
                )
                markk.save()"""
            print("file open success")

        return render(request, 'index.html')