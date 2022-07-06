from django.db import models
from django.contrib.auth.models import AbstractUser
from .utils import CustomUserManager


class User(AbstractUser):
    email           = models.EmailField(unique=True)
    first_name      = models.CharField(max_length=50)
    last_name       = models.CharField(max_length=50)
    is_seller       = models.BooleanField()
    date_joined     = models.DateTimeField(auto_now=True)
    username        = models.CharField(max_length = 55,unique=False, null = True)
    USERNAME_FIELD  = "email"
    REQUIRED_FIELDS = ["first_name","last_name"]
    objects         = CustomUserManager()

