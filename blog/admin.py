from django.contrib import admin

from blog.models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_published', 'views_count')
    search_fields = ('title', 'is_published')


