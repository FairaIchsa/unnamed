from .api_views import EventModelViewSet

from rest_framework.routers import DefaultRouter

app_name = 'event'

router = DefaultRouter()
router.register(r'events', EventModelViewSet, basename='event')
urlpatterns = router.urls
