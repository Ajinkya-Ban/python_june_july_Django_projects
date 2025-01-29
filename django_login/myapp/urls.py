
from django.contrib import admin
from django.urls import path
from .views import signup,login,index,logout_view
urlpatterns = [

    path('signup/',signup, name="signup"),
    path('login/',login,name="login"),
path('index/',index,name="index"),
path('logout/', logout_view, name='logout'),
]
