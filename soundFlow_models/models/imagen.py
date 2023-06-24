from django.db import models

from soundFlow_models.models import Prueba


class Imagen(models.Model):
    prueba = models.ForeignKey(Prueba, on_delete=models.CASCADE, related_name='imagenes')
    imagen = models.ImageField(upload_to='imagenes/')
