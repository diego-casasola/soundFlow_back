from django.db import models

from soundFlow_models.models import Nivel


class Desafio(models.Model):
    nombre = models.CharField(max_length=200)
    nivel = models.ForeignKey(Nivel, on_delete=models.CASCADE, null=True, blank=True)
    min_energia = models.IntegerField(default=5)

    # str method show nivel + nombre
    def __str__(self):
        return str(self.nivel) + ' - ' + self.nombre