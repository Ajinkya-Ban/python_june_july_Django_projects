from django.db import models


# Create your models here.
class CarDetails(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    price = models.IntegerField()
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.name
