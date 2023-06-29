from django.db import models

from authentication.models import User
from soundFlow_models.models import Prueba


class PruebasResueltasUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pruebas_resueltas_user')
    prueba = models.ForeignKey(Prueba, on_delete=models.CASCADE, related_name='pruebas_resueltas_user')
    is_resuelta = models.BooleanField(default=False)