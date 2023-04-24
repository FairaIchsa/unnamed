from rest_framework import views, generics, permissions, status
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView
from unnamed import settings
from .serializers import (CookieTokenRefreshSerializer, UserCreateSerializer, UserDataUpdateSerializer,
                          UserPasswordUpdateSerializer, UserFullDataRetrieveSerializer,
                          )


def set_cookie(response):
    if response.data.get('refresh'):
        response.set_cookie(key=settings.SIMPLE_JWT['AUTH_COOKIE_REFRESH'],
                            value=response.data['refresh'],
                            max_age=settings.SIMPLE_JWT['REFRESH_TOKEN_LIFETIME'],
                            secure=settings.SIMPLE_JWT['AUTH_COOKIE_SECURE'],
                            httponly=settings.SIMPLE_JWT['AUTH_COOKIE_HTTP_ONLY'],
                            samesite=settings.SIMPLE_JWT['AUTH_COOKIE_SAMESITE'])
        del response.data['refresh']


class CookieTokenObtainPairView(TokenObtainPairView):
    def finalize_response(self, request, response, *args, **kwargs):
        set_cookie(response)
        return super().finalize_response(request, response, *args, **kwargs)


class CookieTokenRefreshView(TokenRefreshView):
    def finalize_response(self, request, response, *args, **kwargs):
        set_cookie(response)
        return super().finalize_response(request, response, *args, **kwargs)

    serializer_class = CookieTokenRefreshSerializer


class UserCreateAPIView(generics.CreateAPIView):
    serializer_class = UserCreateSerializer


class UserShortDataRetrieveAPIView(generics.RetrieveAPIView):
    from api.user.serializers import UserListSerializer as UserShortDataRetrieveSerializer

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

    def get_serializer(self, *args, **kwargs):
        return UserPasswordUpdateSerializer(*args, **kwargs)

    def put(self, request):
        user = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        old_password = serializer.data.get("old_password")
        if not user.check_password(old_password):
            return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)

        user.set_password(serializer.data.get("new_password"))
        user.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
