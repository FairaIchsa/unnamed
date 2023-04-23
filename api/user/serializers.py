from django.utils import timezone
from rest_framework import serializers
from mainapp.models.user_models import User


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'image', 'name']


class UserRetrieveSerializer(serializers.ModelSerializer):
    from api.event.serializers import EventListSerializer

    class Meta:
        model = User
        fields = ['id', 'image', 'name', 'gender', 'age', 'following', 'followed', 'host_of', 'participant_of']

    gender = serializers.CharField(source='get_gender_display')
    age = serializers.SerializerMethodField()
    following = UserListSerializer(many=True)
    followed = UserListSerializer(many=True)
    host_of = EventListSerializer(many=True)
    participant_of = EventListSerializer(many=True)

    @staticmethod
    def get_age(user):
        return int((timezone.now().date() - user.birthday).days / 365.2425) if user.birthday is not None else None