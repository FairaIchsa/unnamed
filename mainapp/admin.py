from django.contrib import admin

from mainapp.models.event_models import Event
from mainapp.models.user_models import User


admin.site.register(Event)
admin.site.register(User)
