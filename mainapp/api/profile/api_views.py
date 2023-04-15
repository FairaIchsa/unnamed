from rest_framework import generics
from .serializers import UserListSerializer, UserRetrieveSerializer
from mainapp.models.user_models import User


class UserListAPIView(generics.ListAPIView):
    serializer_class = UserListSerializer

    def get_queryset(self):
        search = self.request.query_params['search'] if 'search' in self.request.query_params else ''
        queryset = User.objects.filter(name__contains=search) | User.objects.filter(email__contains=search)
        return queryset


class UserRetrieveAPIView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserRetrieveSerializer
