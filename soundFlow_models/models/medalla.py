from django.db import models


class Medalla(models.Model):
    nombre = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='medallas/', null=True, blank=True)
