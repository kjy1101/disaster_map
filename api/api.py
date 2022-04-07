from rest_framework import routers

from .viewsets import MarkViewSet

router = routers.DefaultRouter()
router.register(r"markers", MarkViewSet)

urlpatterns = router.urls
