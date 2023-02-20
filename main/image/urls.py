from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r"upload_image", views.UploadImageViewSet, "upload_image")
router.register(r"list_image", views.ImageListViewSet, "list_image")

urlpatterns = [
    path("", include(router.urls)),
]
