from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('car_list', views.car_list, name="list"),
    path('car_list/<int:pk>', views.car_details, name="car_details")
]
