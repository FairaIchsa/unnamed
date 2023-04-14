from django.urls import path, include

app_name = 'api'

urlpatterns = [
    # path('event/', include('mainapp.api.event.urls', namespace='event')),
    # path('auth/', include('mainapp.api.auth.urls', namespace='auth')),
    path('profile/', include('mainapp.api.profile.urls', namespace='profile'))
]
