from django.urls import path

from .api_views import CategoryListAPIView

app_name = 'category'

urlpatterns = [
    path('', CategoryListAPIView.as_view(), name='all'),
]
