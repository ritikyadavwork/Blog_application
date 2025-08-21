from django.db.models.signals import post_save
from notifications.signals import notify
from blogapp.models import Post, Category, Comment
