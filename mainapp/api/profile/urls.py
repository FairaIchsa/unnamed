from django.urls import path

from .api_views import UserListAPIView, UserRetrieveAPIView

app_name = 'profile'

urlpatterns = [
    path('', UserListAPIView.as_view(), name='all'),
    path('<int:pk>', UserRetrieveAPIView.as_view(), name='by-id'),

    # path('<int:pk>/follow', _.as_view(), name='follow'),
    # path('<int:pk>/unfollow', _.as_view(), name='unfollow'),

    # path('get_user_data/', UserDataAPIView.as_view(), name='info'),
    # path('update_user_data/', UpdateUserDataAPIView.as_view(), name='update'),
    # path('update_user_password/', UpdateUserPasswordAPIView.as_view(), name='update-password'),
]
