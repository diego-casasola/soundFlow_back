from django.db import models


class Nivel(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=200)
    nivel = models.IntegerField(default=1)
    imagen = models.ImageField(upload_to='nivel', null=True, blank=True)

    def __str__(self):
        return 'Nivel ' + str(self.nivel) + ' - ' + self.nombre
