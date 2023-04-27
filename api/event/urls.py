from django.urls import path
from .api_views import (EventCreateAPIView, EventListAPIView, EventRetrieveAPIView, EventUpdateAPIVIew,
                        EventDestroyAPIView, EventParticipateAPIView, EventCancelParticipationAPIView,
                        EventKickParticipantAPIView)

app_name = 'event'

urlpatterns = [
    path('create/', EventCreateAPIView.as_view(), name='create'),
    path('', EventListAPIView.as_view(), name='all'),
    path('<int:pk>/', EventRetrieveAPIView.as_view(), name='by-id'),
    path('<int:pk>/update/', EventUpdateAPIVIew.as_view(), name='update'),
    path('<int:pk>/delete/', EventDestroyAPIView.as_view(), name='delete'),
    path('<int:pk>/participate/', EventParticipateAPIView.as_view(), name='participate'),
    path('<int:pk>/cancel_participation/', EventCancelParticipationAPIView.as_view(), name='cancel-participation'),
    path('<int:pk>/kick_participant/', EventKickParticipantAPIView.as_view(), name='kick-participant')
]
