from django.db import models

from soundFlow_models.models import Nivel


class Desafio(models.Model):
    nombre = models.CharField(max_length=50)
    nivel = models.ForeignKey(Nivel, on_delete=models.CASCADE, null=True, blank=True)
    min_energia = models.IntegerField(default=5)

