from django.urls import path, include

app_name = 'api'

urlpatterns = [
    # path('auth/', include('mainapp.api.auth.urls', namespace='auth')),
    path('category/', include('mainapp.api.category.urls', namespace='category')),
    # path('event/', include('mainapp.api.event.urls', namespace='event')),
    path('profile/', include('mainapp.api.profile.urls', namespace='profile')),
]
