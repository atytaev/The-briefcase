from django.contrib import admin
from .models import Sessionals
from django.utils import timezone

@admin.register(Sessionals)
class SessionAdmin(admin.ModelAdmin):
    list_display = ('film', 'start_time', 'hall', 'available_seats', 'is_active')
    search_fields = ('film__title', 'hall')
    list_filter = ('start_time', 'film')

    def is_active(self, obj):
        return obj.start_time > timezone.now()
    is_active.boolean = True
    is_active.short_description = 'Active'