from django.contrib import admin
from .models import Post, Category, Comment, UserProfile


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title']


@admin.register(Category)
class PostAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ["Author", "comment"]
    search_fields = ['Author']


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ['name']
