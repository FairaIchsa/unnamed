from rest_framework import serializers

from mainapp.models.event_models import Event


class EventListSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = Event
        fields = ['id', 'title', 'category', 'location', 'time']
