from django.db import models

from soundFlow_models.models import Prueba


class Audio(models.Model):
    prueba = models.ForeignKey(Prueba, on_delete=models.CASCADE, related_name='audios')
    audio = models.FileField(upload_to='audios/')
