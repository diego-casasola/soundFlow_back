from django.db import models

from soundFlow_models.models import Desafio


class Trofeo(models.Model):
    nombre = models.CharField(max_length=50)
    desafio = models.ForeignKey(Desafio, on_delete=models.CASCADE, related_name='trofeos')
    imagen = models.ImageField(upload_to='trofeos/', null=True, blank=True)