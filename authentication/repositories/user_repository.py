from authentication.models import User
from soundFlow_models.models import UserNivel, Nivel, Desafio


def enable_basic_level(user) -> bool:
    if user:
        try:
            nivel_1 = Nivel.objects.get(nivel=1)
            desafio_1 = Desafio.objects.get(id=19, nivel=nivel_1)
            UserNivel.objects.create(user_id=user['id'], nivel=nivel_1, desafio=desafio_1)
            return True
        except Exception as e:
            User.objects.get(pk=user['id']).delete()
            return False
