from django.db import models


# Create your models here.
class CarDetails(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    price = models.IntegerField()
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class CustomerDetails(models.Model):
    cust_name = models.CharField(max_length=60)
    mobile = models.CharField(max_length=10)
    email = models.EmailField()
    city = models.CharField(max_length=20)
    car = models.ForeignKey(CarDetails, on_delete=models.CASCADE, related_name="customers")

    def __str__(self):
        return self.name