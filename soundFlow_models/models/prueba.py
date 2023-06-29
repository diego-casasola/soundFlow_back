from django.db import models

from soundFlow_models.models import Desafio


# son los datos que se mandaran para realizar la prueba, por ejemplo: se pide que el
# usuario asocie las notas musicales con su nombre correspondiente, como salida se mandará:
# datos = "C_prueba, D, E, F, G, A, B"
# esto en el front lo que hará será mostrar unos inputs, los cuales contendrán las notas musicales en su notación
# anglosajona, el usuario deberá ingresar el nombre de la nota en cada input, por ejemplo:
# do, re, mi, fa, sol, la, si, el resultado seteado en la base de datos será:
# resultado = "do, re, mi, fa, sol, la, si", si los resultados del front coinciden con los de la base de datos
# la prueba se considerará como aprobada

#datos = "C, D, E, F, G, A, B"
#C:do, D:re
#
class Prueba(models.Model):
    datos = models.TextField()
    resultado = models.TextField()
    desafio = models.ForeignKey(Desafio, on_delete=models.CASCADE, related_name='pruebas')
