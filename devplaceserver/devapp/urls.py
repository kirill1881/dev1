from django.conf.urls import include
from django.contrib import admin
from . import views
from django.urls import path

urlpatterns = [
    path('add/', views.add_user),
    path('get/all', views.get_all_users),
]