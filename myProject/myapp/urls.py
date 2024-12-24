
from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [

    path('home/',getHomePage, name="home"),
    path('register/',getRegisterPage, name="register"),
    path('product/',getProductPage, name="product"),
    path('contact/',getContactPage, name="contact")
]