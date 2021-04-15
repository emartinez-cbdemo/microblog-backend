from django.conf.urls import url, include
from django.contrib.auth.models import User
from django.urls import path
from rest_framework import routers
from .views import UserViewSet, Me, create_auth

router = routers.DefaultRouter()
router.register(r"me", Me)
router.register(r"", UserViewSet)

urlpatterns = [
    path("register/", create_auth, name="register"),
    path("", include(router.urls)),
]
