from django.views.generic.base import TemplateView
from rest_framework import viewsets
from rest_framework_gis import filters

from .models import Mark
from .serializers import MarkSerializer

from rest_framework.views import APIView
from .main import tweet_main

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