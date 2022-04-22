from django.contrib.gis import admin

from .models import Mark, DisasterTag, Tweet


@admin.register(Mark)
class MarkAdmin(admin.OSMGeoAdmin):
    list_display = ("name", "location", "region_name")


admin.site.register(DisasterTag)


@admin.register(Tweet)
class TweetAdmin(admin.OSMGeoAdmin):
    list_display = ("twid", "time", "text", "user", "disaster_tag", "location")