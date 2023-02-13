from django.urls import path

from .api_views import SignUpAPIView, LogInAPIView, LogOutAPIView, GetCSRFTokenAPIView


app_name = 'auth'

urlpatterns = [
    path('register/', SignUpAPIView.as_view(), name='register'),
    path('login/', LogInAPIView.as_view(), name='login'),
    path('logout/', LogOutAPIView.as_view(), name='logout'),
    path('csrf_cookie/', GetCSRFTokenAPIView.as_view(), name='csrf-cookie'),
]
