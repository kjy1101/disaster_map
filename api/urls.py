from django.urls import path, include

from .views import MapView
from rest_framework import routers

from .viewsets import MarkViewSet

app_name = "markers"

router = routers.DefaultRouter()
router.register(r"markers", MarkViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path("map/", MapView.as_view()),
]
