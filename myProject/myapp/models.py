from django.db import models
from django.core.exceptions import ValidationError

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
    gender = models.CharField(max_length=10, default=None)
    mobile = models.BigIntegerField()
    email = models.EmailField()
    address = models.TextField()
    country =  models.CharField(max_length=15)
    state = models.CharField(max_length=15)
    city = models.CharField(max_length=15)
    profile_image = models.ImageField(upload_to="media/profile_photos", default="")


    class Meta:
        verbose_name_plural = 'Register'
    def __str__(self):
        return self.fullname

    def clean(self):
        if Register.objects.filter(email=self.email).exclude(pk=self.pk).exists():
            raise ValidationError({"email":"email already exists"})

        if Register.objects.filter(mobile=self.mobile).exclude(pk=self.pk).exists():
            raise ValidationError({"mobile": "mobile number already exists"})

    def save(self, *args, **kwargs):
        self.full_clean()
        super(Register, self).save(*args, **kwargs)

