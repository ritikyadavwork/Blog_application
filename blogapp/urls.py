from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import path, include
from .views import homeView, postBlog_view, blogList_view, blogDetail_view, update_View, update_comment_View, \
    delete_post_view, uploadProfile_view, profile_view, about_view

app_name = 'blogapp'

urlpatterns = [
    path('', homeView, name='home'),
    path('blog-view/', login_required(postBlog_view), name='blog'),
    path('blog-list/', blogList_view, name='blogDetail'),
    path('blogs/category/<str:category>/', blogList_view, name='blog_list_category'),
    path('blog-deatil/<int:post_id>/', blogDetail_view, name='fullDetail'),
    path('update/<int:comment_id>/', update_View, name='update'),
    path('update/update-comment/<int:comment_id>/', update_comment_View, name='updateComment'),
    path('delete/<int:delete_id>/', delete_post_view, name='delete'),
    path('profile/', uploadProfile_view, name='profile'),
    path('profile-view/', profile_view, name='profile_view'),
    path('about-us/', about_view, name='about_us'),

]
