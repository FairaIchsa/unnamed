from django.urls import path, include

app_name = 'mainapp'

urlpatterns = [
    path('api/', include('mainapp.api.urls', namespace='api')),
]
