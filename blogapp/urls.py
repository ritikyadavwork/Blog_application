from django.contrib import admin
from django.urls import path, include
from .views import homeView

app_name = 'blogapp'

urlpatterns = [
    path('home/', homeView, name='home')
]
