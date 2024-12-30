from django.db import models

# Create your models here.

class Contact(models.Model):

    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    mobile = models.BigIntegerField()
    email = models.CharField(max_length=60)
    message = models.TextField()

    def __str__(self):
        return self.fname +" "+self.lname
