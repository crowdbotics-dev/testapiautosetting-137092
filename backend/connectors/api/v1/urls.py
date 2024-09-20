from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import Testconnectors137092ViewSet

router = DefaultRouter()
router.register(
    "testconnectors137092", Testconnectors137092ViewSet, basename="testconnectors137092"
)

urlpatterns = [
    path("connectors/", include(router.urls)),
]
