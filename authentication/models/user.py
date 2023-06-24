from django.contrib.auth.models import AbstractUser
from django.db import models

from soundFlow_models.models import Trofeo, Medalla


class User(AbstractUser):
    xp = models.IntegerField(default=0, null=True)
    email = models.EmailField(unique=True)
    energia = models.IntegerField(default=20, null=True)
    trofeos = models.ManyToManyField(Trofeo, blank=True)
    medallas = models.ManyToManyField(Medalla, blank=True)