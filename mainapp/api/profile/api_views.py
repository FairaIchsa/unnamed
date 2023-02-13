from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated

from .serializers import UserDataSerializer


class UserDataAPIView(APIView):
    authentication_classes = (SessionAuthentication, )
    permission_classes = (IsAuthenticated, )

    def get(self, *args, **kwargs):
        user = self.request.user
        serializer = UserDataSerializer(user)
        return Response(serializer.data)


class UpdateUserDataAPIView(APIView):
    authentication_classes = (SessionAuthentication, )
    permission_classes = (IsAuthenticated, )

    def post(self, request):
        data = self.request.data
        user = self.request.user

        user.name = data['name'] if data['name'] is not None else user.name
        user.phone = data['phone'] if data['phone'] is not None else user.phone

        user.save()
        return Response({'status': 'success'})


class UpdateUserPasswordAPIView(APIView):
    authentication_classes = (SessionAuthentication, )
    permission_classes = (IsAuthenticated, )

    def post(self, request):
        user = self.request.user
        data = self.request.data

        new_password = data['new_password']
        user.set_password(new_password)
        return Response({'status': 'success'})
