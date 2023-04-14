from django.urls import path

from .api_views import UserDataAPIView, UpdateUserDataAPIView, UpdateUserPasswordAPIView

app_name = 'profile'

urlpatterns = [
    path('get_user_data/', UserDataAPIView.as_view(), name='info'),
    path('update_user_data/', UpdateUserDataAPIView.as_view(), name='update'),
    path('update_user_password/', UpdateUserPasswordAPIView.as_view(), name='update-password'),
]
