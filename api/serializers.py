from rest_framework_gis import serializers

from .models import Mark


class MarkSerializer(serializers.GeoFeatureModelSerializer):

    class Meta:
        fields = ("id", "name")
        geo_field = "location"
        model = Mark