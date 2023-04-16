from rest_framework import generics, permissions, status, mixins, viewsets
from rest_framework.response import Response
from .serializers import EventCreateUpdateSerializer, EventListSerializer, EventRetrieveSerializer
from mainapp.models.event_models import Event


class EventCreateUpdateViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin, mixins.UpdateModelMixin):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Event.objects.all()
    serializer_class = EventCreateUpdateSerializer

    def perform_create(self, serializer):
        serializer.save(host=self.request.user)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.host != self.request.user:
            return Response(status=status.HTTP_403_FORBIDDEN, data={'detail': 'Is not the host'})
        super().update(request, *args, **kwargs)


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
    permission_classes = [permissions.IsAuthenticated]
    queryset = Event.objects.all()

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.host != self.request.user:
            return Response(status=status.HTTP_403_FORBIDDEN, data={'detail': 'Is not the host'})
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
