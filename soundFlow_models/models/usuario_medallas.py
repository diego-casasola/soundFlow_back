from django.db import models

from authentication.models import User
from soundFlow_models.models import Medalla


class UsuarioMedallas(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    medalla = models.ForeignKey(Medalla, on_delete=models.CASCADE, null=True)
