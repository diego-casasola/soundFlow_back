from django.db import models

from authentication.models import User
from soundFlow_models.models import Trofeo


class UsuarioTrofeos(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='usuario_trofeos')
    trofeo = models.ForeignKey(Trofeo, on_delete=models.CASCADE, related_name='usuario_trofeos', null=True)
