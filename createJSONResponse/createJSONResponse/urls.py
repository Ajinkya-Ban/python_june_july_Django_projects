
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/cars/', include('myapp.urls')) #http://localhost:8000/api/v1/cars/car_list
]
