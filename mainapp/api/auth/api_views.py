from rest_framework import views, generics, permissions, status
from rest_framework.response import Response
from .serializers import UserCreateSerializer, UserDataUpdateSerializer, \
    UserPasswordUpdateSerializer, UserFullDataRetrieveSerializer


class UserCreateAPIView(generics.CreateAPIView):
    serializer_class = UserCreateSerializer


class UserShortDataRetrieveAPIView(generics.RetrieveAPIView):
    from ..profile.serializers import UserListSerializer as UserShortDataRetrieveSerializer

    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserShortDataRetrieveSerializer

    def get_object(self):
        user = self.request.user
        return user


class UserFullDataRetrieveAPIView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserFullDataRetrieveSerializer

    def get_object(self):
        user = self.request.user
        return user


class UserDataUpdateAPIVIew(generics.UpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserDataUpdateSerializer

    def get_object(self):
        user = self.request.user
        return user


class UserPasswordUpdateAPIView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        user = self.request.user
        return user

    def put(self, request):
        user = self.get_object()
        serializer = UserPasswordUpdateSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        old_password = serializer.data.get("old_password")
        if not user.check_password(old_password):
            return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)

        user.set_password(serializer.data.get("new_password"))
        user.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
