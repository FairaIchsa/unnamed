from rest_framework import serializers
from mainapp.models.user_models import User


class CustomChoiceField(serializers.ChoiceField):

    def to_representation(self, obj):
        if obj == '' and self.allow_blank:
            return obj
        return self._choices[obj]

    def to_internal_value(self, data):
        if data == '' and self.allow_blank:
            return ''

        for key, val in self._choices.items():
            if val == data:
                return key
        self.fail('invalid_choice', input=data)


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'name', 'birthday', 'password']
        extra_kwargs = {'password': {'write_only': True},
                        'name': {'required': True},
                        'birthday': {'required': True}, }

    def create(self, validated_data):
        extra_fields = {'name': validated_data['name'], 'birthday': validated_data['birthday']}
        user = User.objects.create_user(validated_data['email'], validated_data['password'], **extra_fields)
        return user


class UserDataUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'name', 'birthday', 'image', 'phone', 'gender']

    gender = CustomChoiceField(choices=User.genders)


class UserPasswordUpdateSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
