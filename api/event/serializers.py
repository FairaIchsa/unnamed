from rest_framework import serializers
from mainapp.models.event_models import Event


class EventCreateUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = ['id', 'title', 'category', 'location', 'description', 'time']


class EventListSerializer(serializers.ModelSerializer):
    from api.user.serializers import UserListSerializer as UserSerializer

    class Meta:
        depth = 1
        model = Event
        fields = ['id', 'title', 'host', 'category', 'location', 'time', 'is_participating']

    host = UserSerializer()
    is_participating = serializers.SerializerMethodField()

    def get_is_participating(self, event):
        request = self.context['request']
        if not request.user.is_authenticated:
            return False
        return event.participants.filter(pk=request.user.pk).exists()


class EventRetrieveSerializer(serializers.ModelSerializer):
    from api.user.serializers import UserListSerializer

    class Meta:
        depth = 1
        model = Event
        fields = ['id', 'title', 'category', 'host', 'participants', 'location', 'description', 'time',
                  'is_participating']

    host = UserListSerializer()
    participants = UserListSerializer(many=True)
    is_participating = serializers.SerializerMethodField()

    def get_is_participating(self, event):
        request = self.context['request']
        if not request.user.is_authenticated:
            return False
        return event.participants.filter(pk=request.user.pk).exists()
