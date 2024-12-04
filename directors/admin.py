from django.contrib import admin
from .models import Director

@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    list_display = ('name', 'birth_date', 'get_photo')
    search_fields = ('name',)
    list_filter = ('birth_date',)

    def get_photo(self, obj):
        return obj.photo.url if obj.photo else 'No photo'
    get_photo.short_description = 'Photo'