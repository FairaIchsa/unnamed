from django.urls import path, include

app_name = 'api'

urlpatterns = [
    path('event/', include('mainapp.api.event.urls', namespace='event')),
]
