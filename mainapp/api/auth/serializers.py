from rest_framework import serializers

from mainapp.models.user_models import User


class SignUpOutputSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'email', 'name', 'phone']
