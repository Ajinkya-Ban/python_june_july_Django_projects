from django.shortcuts import render
from .models import CarDetails, CustomerDetails
# from django.http import JsonResponse

from .api_file.serializers import CarSerializer, CustomerDetailsSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status


# def car_list(req):
#     cars = CarDetails.objects.all()
#     # convert all the object into dictionary format
#     data = {
#         'cars': list(cars.values()),
#     }
#     # print(cars)
#     return JsonResponse(data)
#
# def car_details(req,pk):
#     cars = CarDetails.objects.get(pk=pk)
#     data = {
#         'name':cars.name,
#         'description':cars.description,
#         'price':cars.price,
#         'active': cars.active
#     }
#     return JsonResponse(data)

# @api_view(['GET', 'POST'])
# def car_list(request):
#     if request.method == 'GET':
#         cars = CarDetails.objects.all()
#         serializer = CarSerializer(cars, many=True)
#         return Response(serializer.data)
#     if request.method == 'POST':
#         serializer = CarSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)


# below code can be used for nested serializer
@api_view(['GET', 'POST'])
def car_list(request):
    if request.method == 'GET':
        customer = CustomerDetails.objects.all()
        serializer = CustomerDetailsSerializer(customer, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = CustomerDetailsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def car_details(request, pk):
    if request.method == 'GET':
        try:
            cars = CarDetails.objects.get(pk=pk)
        except:
            return Response({"Error": "car not found"}, status=status.HTTP_204_NO_CONTENT)
        serializer = CarSerializer(cars)
        return Response(serializer.data)
    if request.method == 'PUT':
        cars = CarDetails.objects.get(pk=pk)
        serializer = CarSerializer(cars, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_204_NO_CONTENT)

    if request.method == "DELETE":
        cars = CarDetails.objects.get(pk=pk)
        cars.delete()
        return Response({"message": "data deleted"})
