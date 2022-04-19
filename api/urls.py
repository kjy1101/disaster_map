from django.urls import path, include

from .views import MapView, MarkViewSet, TweetView
from rest_framework import routers

app_name = "markers"

router = routers.DefaultRouter()
router.register(r"markers", MarkViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path("map/", MapView.as_view()),
    path('tweet/', TweetView.as_view())
]
