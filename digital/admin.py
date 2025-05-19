# digital/admin.py
from django.contrib import admin
from .models import BlogPost


class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    fields = ('title', 'content', 'image', 'published')

admin.site.register(BlogPost, BlogPostAdmin)

