import os
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
    address = models.TextField(blank=True, null=True)
    country =  models.CharField(max_length=15)
    state = models.CharField(max_length=15)
    city = models.CharField(max_length=15)
    profile_image = models.ImageField(upload_to="media/profile_photos", default="")


    class Meta:
        verbose_name_plural = 'Register'
    def __str__(self):
        return self.fullname

    def clean(self):
        errors ={}
        if Register.objects.filter(email=self.email).exclude(pk=self.pk).exists():
            errors["email"] = "Email already exists"

        if Register.objects.filter(mobile=self.mobile).exclude(pk=self.pk).exists():
            errors["mobile"] = "Mobile number already exists"
        if errors:
            raise ValidationError(errors)
    def save(self, *args, **kwargs):
        if self.pk:
            existingUser = Register.objects.get(pk = self.pk)
            if existingUser.profile_image and existingUser.profile_image !=self.profile_image:
                if os.path.isfile(existingUser.profile_image.path):
                    os.remove(existingUser.profile_image.path)
        self.full_clean()
        super(Register, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        if self.profile_image:
            if os.path.isfile(self.profile_image.path):
                os.remove(self.profile_image.path)
        super().delete(*args, **kwargs)
