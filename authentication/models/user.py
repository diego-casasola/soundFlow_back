from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    xp = models.IntegerField(default=0, null=True)
    email = models.EmailField(unique=True)