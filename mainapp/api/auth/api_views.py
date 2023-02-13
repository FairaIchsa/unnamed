from django.views.decorators.csrf import ensure_csrf_cookie, csrf_protect
from django.utils.decorators import method_decorator
from django.contrib import auth

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.authentication import BasicAuthentication, SessionAuthentication

from .serializers import *
from mainapp.models.user_models import User


@method_decorator(csrf_protect, name='dispatch')
class SignUpAPIView(APIView):
    permission_classes = (AllowAny,)
    authentication_classes = (BasicAuthentication, SessionAuthentication,)

    def post(self, request):
        data = self.request.data

        email = data['email']
        password = data['password']
        name = data['name'] if 'name' in data else None
        phone = data['phone'] if 'phone' in data else None

        if User.objects.filter(email=email).exists():
            return Response({'error': 'email already exists.'})

        user = User.objects.create_user(
            email=email, password=password, name=name, phone=phone)
        return Response(SignUpOutputSerializer(user).data)


@method_decorator(csrf_protect, name='dispatch')
class LogInAPIView(APIView):
    permission_classes = (AllowAny,)
    authentication_classes = (SessionAuthentication,)

    def post(self, request):
        data = self.request.data

        email = data['email']
        password = data['password']

        user = auth.authenticate(email=email, password=password)

        if user is not None:
            auth.login(request, user)
            return Response({'status': 'authenticated'})
        return Response({'status': 'incorrect input'})


class LogOutAPIView(APIView):
    permission_classes = (AllowAny, )
    authentication_classes = (SessionAuthentication,)

    def post(self, request):
        auth.logout(request)
        return Response({'status': 'logged out'})


@method_decorator(ensure_csrf_cookie, name='dispatch')
class GetCSRFTokenAPIView(APIView):
    permission_classes = (AllowAny, )
    authentication_classes = (SessionAuthentication,)

    def get(self, request):
        return Response({'success':  'CSRF cookie set'})
