from django.urls import path
from. import views
from django.contrib import admin

urlpatterns = [
    path('test/', views.test),
    path('static/', views.static),
    path('', views.index),


    ]