from django.views.generic.base import TemplateView
from rest_framework import viewsets
from rest_framework_gis import filters

from .models import Mark
from .serializers import MarkSerializer

from rest_framework.views import APIView
from .main import tweet_main

import json
from django.shortcuts import render
from django.contrib.gis.geos import Polygon, MultiPolygon
<<<<<<< HEAD

=======
>>>>>>> f65d84f86c74251149c7176de8335c4edac5f8c0

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
            for i in range(len(data["features"])):
                print(data["features"][i]["properties"]["CTP_KOR_NM"], " 정보 표시됨")

                polys = []
                for j in range(len(data["features"][i]["geometry"]["coordinates"])):
                    polys.append(Polygon(data["features"][i]["geometry"]["coordinates"][j]))

                poly = MultiPolygon(polys)
                mark_kr, created = Mark.objects.get_or_create(
                    name = data["features"][i]["properties"]["CTP_KOR_NM"],
                    location=poly
                )
                if created:
                    mark_kr.save()
                else:
                    return mark_kr

            print("file open success")

        return render(request, 'index.html')