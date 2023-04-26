from django.shortcuts import get_object_or_404
from rest_framework import views, generics, permissions, status
from rest_framework.response import Response
from mainapp.models.user_models import User
from .serializers import UserListSerializer, UserRetrieveSerializer
from .permissions import IsNotSelf


class UserListAPIView(generics.ListAPIView):
    serializer_class = UserListSerializer

    def get_queryset(self):
        search = self.request.query_params['search'] if 'search' in self.request.query_params else ''
        queryset = User.objects.filter(name__contains=search) | User.objects.filter(email__contains=search)
        return queryset


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
        # if self.request.user.following.filter(pk=pk).exists():
        #     return Response({'detail': 'Already following.'}, status=status.HTTP_400_BAD_REQUEST)
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
        # if not self.request.user.following.filter(pk=pk).exists():
        #     return Response({'detail': 'Already not following.'}, status=status.HTTP_400_BAD_REQUEST)
        request.user.following.remove(user)
        return Response(status=status.HTTP_204_NO_CONTENT)
