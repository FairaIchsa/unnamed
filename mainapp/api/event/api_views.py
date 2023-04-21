from rest_framework import generics, mixins, viewsets
from .serializers import EventCreateUpdateSerializer, EventListSerializer, EventRetrieveSerializer
from .permissions import IsHostOrReadOnly
from mainapp.models.event_models import Event


class EventCreateUpdateViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin, mixins.UpdateModelMixin):
    permission_classes = [IsHostOrReadOnly]
    queryset = Event.objects.all()
    serializer_class = EventCreateUpdateSerializer

    def perform_create(self, serializer):
        serializer.save(host=self.request.user)


class EventListAPIView(generics.ListAPIView):
    serializer_class = EventListSerializer

    def get_queryset(self):
        search = self.request.query_params['search'] if 'search' in self.request.query_params else ''
        category = self.request.query_params['category'] if 'category' in self.request.query_params else None
        queryset = Event.objects.filter(title__contains=search)
        if category:
            queryset.filter(category=category)
        return queryset


class EventRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Event.objects.all()
    serializer_class = EventRetrieveSerializer


class EventDestroyAPIView(generics.DestroyAPIView):
    permission_classes = [IsHostOrReadOnly]
    queryset = Event.objects.all()
