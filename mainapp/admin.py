from django.contrib import admin

from mainapp.models.event_models import Event, Category
from mainapp.models.user_models import User


admin.site.register(Event)
admin.site.register(Category)
admin.site.register(User)
