from django.urls import path

from .views import MapView

app_name = "markers"

urlpatterns = [
    path("map/", MapView.as_view()),
]
