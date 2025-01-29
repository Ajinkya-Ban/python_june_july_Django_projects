from django.db import models
import bcrypt

# Create your models here.
class Login(models.Model):
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=255)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.password = bcrypt.hashpw(self.password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
            super(Login, self).save(*args, **kwargs)


    def __str__(self):
        return self.username


    # password decrypt code
