from rest_framework import serializers
from ..models import CarDetails, CustomerDetails
import re


def alphanumeric(value):
    if not re.fullmatch(r"[A-Za-z0-9 ]*", value):
        raise serializers.ValidationError("Only alphanumeric characters and spaces are allowed.")


# class CarSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(max_length=50, required=True, validators=[alphanumeric])
#     description = serializers.CharField(max_length=100, required=True)
#     price = serializers.IntegerField(required=True)
#     active = serializers.BooleanField()
#
#     def create(self, validated_data):
#         return CarDetails.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.description = validated_data.get('description', instance.description)
#         instance.price = validated_data.get('price', instance.price)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
#         return instance

def validate_description(value):
    if len(value) < 10:
        raise serializers.ValidationError("description must be greater than 10 char long")
    return value


def validate_price(value):
    if value < 10:
        raise serializers.ValidationError("price must be greater than 10 lacs")
    return value


class CarSerializer(serializers.ModelSerializer):
    name = serializers.CharField(validators=[alphanumeric])

    class Meta:
        model = CarDetails
        # fields = ['name','description']
        fields = "__all__"

    # object level validation
    def validate(self, data):
        if data['name'] == data['description']:
            raise serializers.ValidationError("Name and description must be different")
        return data
    # def validate_name(self,value):
    #     if CarDetails.objects.filter(name=value).exists():
    #         raise serializers.ValidationError("Already exists.")
    #         return value


class CustomerDetailsSerializer(serializers.ModelSerializer):
    car = CarSerializer()  # Nested Serializer

    class Meta:
        model = CustomerDetails
        fields = ['cust_name','mobile','email','city','car']

    def create(self, validated_data):
        car_data = validated_data.pop('car')
        car_instance, created = CarDetails.objects.get_or_create(**car_data) # it will avoid duplication of data
        customer = CustomerDetails.objects.create(car=car_instance, **validated_data)
        return customer

"""
1. validated_data contains the cleaned and validated input data from the request.
2. .pop('car') extracts the car dictionary from validated_data, removing it from the original dictionary.
3. Now, car_data holds the details of the car (like name, description, price), while validated_data holds customer-related information (name, email etc).

4. get_or_create(**car_data) looks for an existing car with the given attributes (name, description, price).
5. If a matching car exists, car_instance is assigned to that car, and created is False.
6. If no matching car is found, a new CarDetails instance is created, and created is True.
7. This prevents duplicate car entries in the database.
"""