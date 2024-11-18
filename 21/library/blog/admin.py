from django.contrib import admin

from .models import Blog, Users

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'publication_year', 'author')
    list_filter = ('publication_year', 'author',)

@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    pass