from django.contrib import admin
from .models import Post, Category, Comment, UserProfile, Like


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ["commented_by"]


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ['name']


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ['post']
