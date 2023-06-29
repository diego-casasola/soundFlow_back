from django.db import models

from authentication.models import User
from soundFlow_models.models import Nivel, Desafio


class UserNivel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_nivel')
    nivel = models.ForeignKey(Nivel, on_delete=models.CASCADE, related_name='user_nivel')
    desafio = models.ForeignKey(Desafio, on_delete=models.CASCADE, related_name='user_nivel')
    is_resuelto = models.BooleanField(default=False)
