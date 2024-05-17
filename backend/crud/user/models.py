from django.db import models
from django.db import models
from django.contrib.auth.models import AbstractUser


from .managers import CustomUserManager
# Custom User Model

class CustomUser(AbstractUser):
    username=None
    email = models.EmailField("email address",unique = True)
    phone = models.IntegerField(unique=True,null=True)
    address = models.CharField(max_length=50,null=True)
    gender = models.CharField(max_length=10)
    isDeleted=models.BooleanField(default=False)
    USERNAME_FIELD="email"
    REQUIRED_FIELDS=[]

    objects = CustomUserManager()

    def __str__(self):
        return super().email

