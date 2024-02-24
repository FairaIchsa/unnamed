from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenRefreshSerializer
from rest_framework_simplejwt.exceptions import InvalidToken
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


class CookieTokenRefreshSerializer(TokenRefreshSerializer):
    refresh = None

    def validate(self, attrs):
        attrs['refresh'] = self.context['request'].COOKIES.get('refresh')
        if attrs['refresh']:
            return super().validate(attrs)
        else:
            raise InvalidToken('No valid token found in cookie \'refresh\'')


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'name', 'birthday', 'password', 'image', 'phone', 'gender']
        extra_kwargs = {'password': {'write_only': True},
                        'name': {'required': True},
                        'birthday': {'required': True}, }

    gender = CustomChoiceField(choices=User.genders)

    def create(self, validated_data):
        extra_fields = {}
        for field in ['name', 'birthday', 'image', 'phone', 'gender']:
            if field in validated_data:
                extra_fields[field] = validated_data[field]
        user = User.objects.create_user(validated_data['email'], validated_data['password'], **extra_fields)
        return user


class UserFullDataRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'name', 'birthday', 'image', 'phone', 'gender', 'description']

    gender = serializers.CharField(source='get_gender_display')


class UserDataUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'name', 'birthday', 'image', 'phone', 'gender', 'description']

    gender = CustomChoiceField(choices=User.genders)


class UserPasswordUpdateSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
