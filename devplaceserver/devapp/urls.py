from django.conf.urls import include
from django.contrib import admin
from . import views
from django.urls import path

urlpatterns = [
    path('', views.index),
    path('add/', views.add_user),

    path('add/rekaso', views.add_rekaso),
]