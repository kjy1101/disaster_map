from django.contrib.gis import admin

from .models import Mark


@admin.register(Mark)
class MarkAdmin(admin.OSMGeoAdmin):
    list_display = ("name", "location")