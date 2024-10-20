from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from random import randint
from .managers import CustomUserManager


def default_image():
    return "images/profilepictures/logo2.png" 

class User(AbstractUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    username = models.CharField(max_length=150, unique=True, blank=True, null=True)
    image = models.ImageField(upload_to='images/profilepictures/', default=default_image, blank=True, null=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    
    objects = CustomUserManager()

    def save(self, *args, **kwargs):
        if not self.username:
            username_base = self.email.split("@")[0]
            username = username_base
            counter = 1
            while User.objects.filter(username=username).exists():
                username = f"{username_base}{counter}"
                counter += 1
            self.username = username
        super().save(*args, **kwargs) 

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username if self.username else self.email
    