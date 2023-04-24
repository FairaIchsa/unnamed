from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from mainapp.models.event_models import Event, Category
from mainapp.models.user_models import User


class EventAdmin(admin.ModelAdmin):
    model = Event
    exclude = ['participants']


class UserAdminConfig(UserAdmin):
    model = User
    search_fields = ('email', 'name')
    list_filter = ('is_active', 'is_staff', 'is_superuser', 'groups')
    list_display = ('email', 'name', 'is_staff')
    ordering = ('-date_joined',)
    fieldsets = (
        (None, {'fields': ('image', 'email', 'name', 'birthday', 'gender', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {'fields': ('image', 'email', 'name', 'birthday', 'gender', 'password1', 'password2')}),
        ('Permissions', {'fields': ('is_staff',)}),
    )


admin.site.register(Event, EventAdmin)
admin.site.register(Category)
admin.site.register(User, UserAdminConfig)
