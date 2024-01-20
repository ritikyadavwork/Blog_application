from django.contrib import admin
from .models import Post, category, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title']


@admin.register(category)
class PostAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ["Author", "comment"]
    search_fields = ['Author']
