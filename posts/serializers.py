from .models import Post
from rest_framework import serializers
from users.serializers import UserSerializer


class PostSerializerGET(serializers.HyperlinkedModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Post
        fields = ["url", "user", "message", "timestamp"]


class PostSerializerPOST(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ["url", "user", "message", "timestamp"]
