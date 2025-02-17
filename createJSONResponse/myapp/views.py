from django.shortcuts import render
from .models import CarDetails
from django.http import JsonResponse


def car_list(req):
    cars = CarDetails.objects.all()
    # convert all the object into dictionary format
    data = {
        'cars': list(cars.values()),
    }
    # print(cars)
    return JsonResponse(data)

def car_details(req,pk):
    cars = CarDetails.objects.get(pk=pk)
    data = {
        'name':cars.name,
        'description':cars.description,
        'price':cars.price,
        'active': cars.active
    }
    return JsonResponse(data)