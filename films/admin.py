from django.contrib import admin
from .models import Film

@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    list_display = ('title', 'release_date', 'duration', 'get_genre', 'get_director')
    search_fields = ('title', 'description')
    list_filter = ('release_date', 'genre')

    filter_horizontal = ('actors','genre',)
    def get_genre(self, obj):
        return ", ".join([genre.name for genre in obj.genre.all()])
    get_genre.short_description = 'Genres'

    def get_director(self, obj):
        return obj.director.name if obj.director else 'No director'
    get_director.short_description = 'Director'