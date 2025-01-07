
from django.urls import path
from .views import *


urlpatterns = [

    path('home/', getHomePage, name="home"),
    path('register/', getRegisterPage, name="register"),
    path('product/', getProductPage, name="product"),
    path('contact/', getContactPage, name="contact"),
    path('submit_contact/', submit_contact, name="submit_contact"),
    path('submit_register/', submit_register, name="submit_register")

]


