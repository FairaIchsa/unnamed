from rest_framework import generics
from .serializers import UserListSerializer, UserRetrieveSerializer
from mainapp.models.user_models import User


class UserListAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer


class UserRetrieveAPIView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserRetrieveSerializer
