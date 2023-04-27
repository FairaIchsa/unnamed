from django.shortcuts import get_object_or_404
from rest_framework import views, generics, permissions, status, filters
from rest_framework.response import Response
from mainapp.models.event_models import Event
from mainapp.models.user_models import User
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
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', '=host__name']

    def get_queryset(self):
        queryset = Event.objects.all()
        category = self.request.query_params.get('category', None)
        if category and category.isdigit():
            queryset = queryset.filter(category=category)
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
        event.participants.remove(request.user)
        return Response(status=status.HTTP_204_NO_CONTENT)


class EventKickParticipantAPIView(views.APIView):
    permission_classes = [permissions.IsAuthenticated, IsHost]

    def get_object(self):
        obj = get_object_or_404(Event, pk=self.kwargs['pk'])
        self.check_object_permissions(self.request, obj)
        return obj

    def post(self, request, pk):
        pk_ = request.query_params['id']
        user = get_object_or_404(User, pk=pk_)
        event = self.get_object()
        event.participants.remove(user)
        return Response(status=status.HTTP_204_NO_CONTENT)
