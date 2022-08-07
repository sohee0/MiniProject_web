from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('beach/', include('BeachData.urls')),
    path('map/', include('map.urls')),]


