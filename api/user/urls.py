from django.urls import path
from .api_views import UserListAPIView, UserRetrieveAPIView, UserFollowAPIView, UserUnfollowAPIView

app_name = 'profile'

urlpatterns = [
    path('', UserListAPIView.as_view(), name='all'),
    path('<int:pk>/', UserRetrieveAPIView.as_view(), name='by-id'),
    path('<int:pk>/follow/', UserFollowAPIView.as_view(), name='follow'),
    path('<int:pk>/unfollow/', UserUnfollowAPIView.as_view(), name='unfollow'),
]
