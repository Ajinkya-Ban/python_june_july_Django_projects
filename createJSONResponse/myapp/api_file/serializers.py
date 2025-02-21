from rest_framework import serializers
from ..models import CarDetails


def alphanumeric(value):
    updated_str = value
    if not str(updated_str).isalnum() and str(updated_str).isspace():
        raise serializers.ValidationError("Only alphanumeric characters allowed")


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

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarDetails
        # fields = ['name','description']
        fields = "__all__"


    def validate_price(self, value):
        if value < 10:
            raise serializers.ValidationError("price must be greater than 10 lacs")
        return value

    def validate_description(self, value):
        if len(value) < 10:
            raise serializers.ValidationError("description must be greater than 10 char long")
        return value

    # object level validation
    def validate(self, data):
        if data['name'] == data['description']:
            raise serializers.ValidationError("Name and description must be different")
        return data
