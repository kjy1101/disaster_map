"""Markers API views."""
from rest_framework import viewsets
from rest_framework_gis import filters

from .models import Mark
from .serializers import MarkSerializer


class MarkViewSet(viewsets.ReadOnlyModelViewSet):
    """Marker view set."""

    bbox_filter_field = "location"
    filter_backends = (filters.InBBoxFilter,)
    queryset = Mark.objects.all()
    serializer_class = MarkSerializer
