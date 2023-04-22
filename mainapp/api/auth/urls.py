from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .api_views import UserCreateAPIView, UserShortDataRetrieveAPIView, UserFullDataRetrieveAPIView, \
    UserDataUpdateAPIVIew, UserPasswordUpdateAPIView


app_name = 'auth'

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='token-obtain-pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
    path('register/', UserCreateAPIView.as_view(), name='register'),
    path('get_short_user_data/', UserShortDataRetrieveAPIView.as_view(), name='get-short-user-data'),
    path('get_full_user_data/', UserFullDataRetrieveAPIView.as_view(), name='get-full-user-data'),
    path('update_user_data/', UserDataUpdateAPIVIew.as_view(), name='update-user-data'),
    path('update_user_password/', UserPasswordUpdateAPIView.as_view(), name='update-user-password'),
    # path('delete_user/', UserDestroyAPIView.as_view(), name='destroy-user'),
    # path('logout/', LogOutAPIView.as_view(), name='logout'),
]
