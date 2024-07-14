from django.conf.urls import include
from django.contrib import admin
from . import views
from django.urls import path

urlpatterns = [
    path('', views.index),
    path('add/', views.add_user),
    path('get/all', views.get_all_users),
    path('/get/all/managers', views.get_all_managers),
    path('add/rekaso', views.add_rekaso),
]