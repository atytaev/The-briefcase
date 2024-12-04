from django.contrib import admin
from .models import Actor

@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ('name', 'birth_date', 'get_photo')
    search_fields = ('name',)
    list_filter = ('birth_date',)

    def get_photo(self, obj):
        return obj.photo.url if obj.photo else 'No photo'
    get_photo.short_description = 'Photo'