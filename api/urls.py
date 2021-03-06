from django.urls import path, include

from .views import MapView, MarkViewSet, BoundarySet
from rest_framework import routers

app_name = "markers"

router = routers.DefaultRouter()
router.register(r"markers", MarkViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path("map/", MapView.as_view()),
    path('boundary/', BoundarySet.as_view())
]
