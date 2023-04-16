from rest_framework import generics
from mainapp.models.event_models import Category
from .serializers import CategoryListSerializer


class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer
