from rest_framework import serializers

from mainapp.models.event_models import Event


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['id', 'name', 'location', 'description']
