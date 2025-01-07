from django.db import models


# Create your models here.

class Contact(models.Model):

    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    mobile = models.BigIntegerField()
    email = models.CharField(max_length=60)
    message = models.TextField()

    class Meta:
        verbose_name_plural = 'Contact'

    def __str__(self):
        return self.fname + " " + self.lname


class Register(models.Model):
    fullname = models.CharField(max_length=50, null=True, blank=False)
    mobile = models.BigIntegerField()
    email = models.CharField(max_length=80)
    address = models.TextField()
    country =  models.CharField(max_length=15)
    state = models.CharField(max_length=15)
    city = models.CharField(max_length=15)
    profile_image = models.ImageField(upload_to="profile_photos/", default="")

    class Meta:
        verbose_name_plural = 'Register'
    def __str__(self):
        return self.fullname

