from django.contrib.auth.models import User
from rest_framework import viewsets, status, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import UserSerializer, UserCreateSerializer
from .permissions import IsAccountAdminOrReadOnly


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAccountAdminOrReadOnly]


class Me(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def get_queryset(self):
        queryset = User.objects.filter(username=self.request.user.username)
        return queryset


@api_view(["POST"])
@permission_classes((permissions.AllowAny,))
def create_auth(request):
    serialized = UserCreateSerializer(data=request.data, context={"request": request})
    if serialized.is_valid():
        User.objects.create_user(
            serialized.data["username"],
            serialized.data["email"],
            serialized.data["password"],
        )
        return Response(serialized.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serialized._errors, status=status.HTTP_400_BAD_REQUEST)
