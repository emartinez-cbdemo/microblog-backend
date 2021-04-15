from rest_framework import viewsets
from .models import Post
from .serializers import PostSerializerGET, PostSerializerPOST
from .permissions import IsAccountAdminOrReadOnly
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializerGET
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        if self.request.method == "POST":
            return PostSerializerPOST
        return PostSerializerGET
