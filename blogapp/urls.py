from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import path, include
from .views import homeView, postBlog_view, blogList_view, blogDetail_view

app_name = 'blogapp'

urlpatterns = [
    path('', homeView, name='home'),
    path('blog-view/', login_required(postBlog_view), name='blog'),
    path('blog-list/', blogList_view, name='blogDetail'),
    path('blog-deatil/<int:post_id>/', blogDetail_view, name='fullDetail'),
]
