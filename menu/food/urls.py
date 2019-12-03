from django.urls import path
from . import views
from .views import *
from rest_framework import routers 
from django.contrib import admin
from django.urls import path, include                   # add this


urlpatterns = [
    path('<str:id>/', views.get_restaurant_information),
    path('<str:id>/<str:foodid>/',views.get_food_information)


]
