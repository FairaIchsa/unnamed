from rest_framework import serializers
from mainapp.models.event_models import Event


class EventCreateUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = ['id', 'title', 'category', 'location', 'description', 'time']


class EventListSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = Event
        fields = ['id', 'title', 'category', 'location', 'time']


class EventRetrieveSerializer(serializers.ModelSerializer):
    from api.user.serializers import UserListSerializer

    class Meta:
        depth = 1
        model = Event
        fields = ['id', 'title', 'category', 'host', 'participants', 'location', 'description', 'time']

    host = UserListSerializer()
    participants = UserListSerializer(many=True)
