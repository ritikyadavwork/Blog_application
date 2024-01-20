from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import path, include
from .views import homeView, postBlog_view, blogDetail_view, postBlogDetail_view

app_name = 'blogapp'

urlpatterns = [
    path('', homeView, name='home'),
    path('blog-view/', login_required(postBlog_view), name='blog'),
    path('blog-detail/', blogDetail_view, name='blogDetail'),
    path('full-deatil/<int:post_id>/', postBlogDetail_view, name='fullDetail'),
]
