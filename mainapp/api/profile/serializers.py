from rest_framework import serializers

from mainapp.models.user_models import User


class UserDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'phone', 'email']