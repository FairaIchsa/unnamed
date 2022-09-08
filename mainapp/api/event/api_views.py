from rest_framework.viewsets import ModelViewSet

from .serializers import EventSerializer
from mainapp.models.event_models import Event


class EventModelViewSet(ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
