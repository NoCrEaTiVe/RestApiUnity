from django.urls import path
from . import views
from .views import *
from rest_framework import routers 
from django.contrib import admin
from django.urls import path, include                   # add this


urlpatterns = [
    path('vidoes/', views.videos),
    path('upload/', FileUploadView.as_view()),
    path('get_videos/', views.get_videos),
    path('delete/',views.delete_videos)


]
