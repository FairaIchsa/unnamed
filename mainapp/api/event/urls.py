from django.urls import path
from .api_views import EventCreateUpdateViewSet, EventListAPIView, EventRetrieveAPIView, EventDestroyAPIView\

app_name = 'event'

urlpatterns = [
    path('create', EventCreateUpdateViewSet.as_view({'post': 'create'}), name='create'),
    path('', EventListAPIView.as_view(), name='all'),
    path('<int:pk>', EventRetrieveAPIView.as_view(), name='by-id'),
    path('<int:pk>/update', EventCreateUpdateViewSet.as_view({'put': 'update'}), name='update'),
    path('<int:pk>/delete', EventDestroyAPIView.as_view(), name='delete'),
]
