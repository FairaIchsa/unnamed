from django.shortcuts import get_object_or_404
from rest_framework import views, generics, permissions, status
from rest_framework.response import Response
from mainapp.models.event_models import Event
from .serializers import EventCreateUpdateSerializer, EventListSerializer, EventRetrieveSerializer
from .permissions import IsHost, IsNotHost


class EventCreateAPIView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Event.objects.all()
    serializer_class = EventCreateUpdateSerializer

    def perform_create(self, serializer):
        return serializer.save(host=self.request.user)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = self.perform_create(serializer)
        instance_serializer = EventRetrieveSerializer(instance)
        return Response(instance_serializer.data)


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


class EventUpdateAPIVIew(generics.UpdateAPIView):
    permission_classes = [permissions.IsAuthenticated, IsHost]
    queryset = Event.objects.all()
    serializer_class = EventCreateUpdateSerializer

    def perform_update(self, serializer):
        return serializer.save(host=self.request.user)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        partial = kwargs.pop('partial', False)
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        instance = self.perform_update(serializer)
        instance_serializer = EventRetrieveSerializer(instance)
        return Response(instance_serializer.data)


class EventDestroyAPIView(generics.DestroyAPIView):
    permission_classes = [permissions.IsAuthenticated, IsHost]
    queryset = Event.objects.all()


class EventParticipateAPIView(views.APIView):
    permission_classes = [permissions.IsAuthenticated, IsNotHost]

    def get_object(self):
        obj = get_object_or_404(Event, pk=self.kwargs['pk'])
        self.check_object_permissions(self.request, obj)
        return obj

    def post(self, request, pk):
        event = self.get_object()
        # if event.participants.filter(pk=request.user.pk).exists():
        #     return Response({'detail': 'Already participating.'}, status=status.HTTP_400_BAD_REQUEST)
        event.participants.add(request.user)
        return Response(status=status.HTTP_204_NO_CONTENT)


class EventCancelParticipationAPIView(views.APIView):
    permission_classes = [permissions.IsAuthenticated, IsNotHost]

    def get_object(self):
        obj = get_object_or_404(Event, pk=self.kwargs['pk'])
        self.check_object_permissions(self.request, obj)
        return obj

    def post(self, request, pk):
        event = self.get_object()
        # if event.participants.filter(pk=request.user.pk).exists():
        #     return Response({'detail': 'Already not participating.'}, status=status.HTTP_400_BAD_REQUEST)
        event.participants.remove(request.user)
        return Response(status=status.HTTP_204_NO_CONTENT)
