from django.shortcuts import get_object_or_404
from rest_framework import views, generics, permissions, status, filters
from rest_framework.response import Response
from mainapp.models.user_models import User
from .serializers import UserListSerializer, UserRetrieveSerializer
from .permissions import IsNotSelf


class UserListAPIView(generics.ListAPIView):
    serializer_class = UserListSerializer
    queryset = User.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', '=email', '=phone']


class UserRetrieveAPIView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserRetrieveSerializer


class UserFollowAPIView(views.APIView):
    permission_classes = [permissions.IsAuthenticated, IsNotSelf]

    def get_object(self):
        obj = get_object_or_404(User, pk=self.kwargs['pk'])
        self.check_object_permissions(self.request, obj)
        return obj

    def post(self, request, pk):
        user = self.get_object()
        request.user.following.add(user)
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserUnfollowAPIView(views.APIView):
    permission_classes = [permissions.IsAuthenticated, IsNotSelf]

    def get_object(self):
        obj = get_object_or_404(User, pk=self.kwargs['pk'])
        self.check_object_permissions(self.request, obj)
        return obj

    def post(self, request, pk):
        user = self.get_object()
        request.user.following.remove(user)
        return Response(status=status.HTTP_204_NO_CONTENT)
