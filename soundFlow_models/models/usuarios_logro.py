from django.db import models

from authentication.models import User
from soundFlow_models.models import Trofeo, Medalla


class UsuarioLogro(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_nivel')
    trofeo = models.ForeignKey(Trofeo, on_delete=models.CASCADE, related_name='user_nivel')
    medalla = models.ForeignKey(Medalla, on_delete=models.CASCADE, related_name='user_nivel')