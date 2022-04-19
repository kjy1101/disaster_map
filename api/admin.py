from django.contrib.gis import admin

from .models import Mark, DisasterTag, Tweet


@admin.register(Mark)
class MarkAdmin(admin.OSMGeoAdmin):
    list_display = ("name", "location")

admin.site.register(DisasterTag)
admin.site.register(Tweet)