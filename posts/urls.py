from django.conf.urls import url, include
from django.contrib.auth.models import User
from django.urls import path
from rest_framework import routers
from .views import PostViewSet

router = routers.DefaultRouter()
router.register(r"", PostViewSet)

urlpatterns = [path("", include(router.urls))]
