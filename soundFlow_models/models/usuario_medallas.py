from django.db import models

from authentication.models import User
from soundFlow_models.models import Medalla


class UsuarioMedallas(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_medallas')
    medalla = models.ForeignKey(Medalla, on_delete=models.CASCADE, related_name='user_medallas', null=True)
