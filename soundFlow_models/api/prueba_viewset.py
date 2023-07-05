from rest_framework import viewsets, serializers, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from authentication.models import User
from soundFlow_models.models import Prueba, Nivel, Desafio, UserNivel, PruebasResueltasUser
from soundFlow_models.repositories.prueba_repository import verify_prueba


class PruebaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prueba
        fields = '__all__'


class PruebaViewSet(viewsets.ModelViewSet):
    queryset = Prueba.objects.all()
    serializer_class = PruebaSerializer

    @action(detail=True, methods=['GET'], url_path='get-pruebas-desafio', url_name='Obtener pruebas por desafio',
            permission_classes=[IsAuthenticated])
    def get_pruebas_desafio(self, request, pk=None):
        if pk is None:
            return Response({'message': 'El desafio no existe'}, status=404)
        try:
            pruebas = Prueba.objects.filter(desafio_id=pk)
            return Response(PruebaSerializer(pruebas, many=True).data)
        except Prueba.DoesNotExist:
            return Response({'message': 'El desafio no existe'}, status=404)

    @action(detail=False, methods=['POST'], url_path='respuesta-pruebaDesafio-user',
            url_name='Respuesta de prueba por desafio', permission_classes=[IsAuthenticated])
    def respuesta_pruebaDesafio_user(self, request):
        if request.user.energia >= 5:
            desafio = request.data['desafio']
            desafio = int(desafio)
            respuestas_user = request.data['prueba_res']

            respuestas_user = sorted(respuestas_user, key=lambda prueba: prueba['id'])
            pruebas_db = Prueba.objects.filter(desafio_id=desafio).order_by('id')

            # inicializar las pruebas resueltas por el usuario si es que no existen
            for prueba in pruebas_db:
                if not PruebasResueltasUser.objects.filter(user_id=request.user.id, prueba_id=prueba.id).exists():
                    PruebasResueltasUser.objects.create(user_id=request.user.id, prueba_id=prueba.id)

            resultado = [respuestas_user for (respuestas_user, pruebas_db) in zip(respuestas_user, pruebas_db) if
                         verify_prueba(respuestas_user, pruebas_db)]

            # actualizar las pruebas resueltas por el usuario
            for prueba in resultado:
                PruebasResueltasUser.objects.filter(user_id=request.user.id, prueba_id=prueba['id']).update(
                    is_resuelta=True)

            # por cada prueba con is_resuelta = True, aumenta la cantidad de XP del usuario
            # for prueba in PruebasResueltasUser.objects.filter(user_id=request.user.id, is_resuelta=True):
            #     User.objects.get(pk=request.user.id).update(xp=request.user.xp + 100)

            resultado = sorted(resultado, key=lambda prueba: prueba['id'])
            nivel = None

            if len(resultado) == len(pruebas_db):
                desafio_actual = UserNivel.objects.get(user_id=request.user.id, desafio_id=desafio)
                user = User.objects.get(pk=request.user.id)
                nivel = Desafio.objects.get(id=desafio).nivel_id
                user.energia = user.energia - 5
                if desafio_actual.is_resuelto is False:
                    print(desafio_actual.is_resuelto)
                    desafio_actual.is_resuelto = True
                    user.xp = user.xp + 100
                    print(user.xp)
                    print(desafio_actual.is_resuelto)
                    desafio_actual.save()
                    list_nivel = UserNivel.objects.filter(user_id=request.user.id, nivel=nivel, is_resuelto=True)
                    if user.xp >= 500 and len(list_nivel) >= 5 and nivel == 1:
                        UserNivel.objects.create(user_id=request.user.id, nivel_id=nivel + 1, desafio_id=24,
                                                 is_resuelto=False)
                    elif user.xp >= 1000 and len(list_nivel) >= 5 and nivel == 2:
                        UserNivel.objects.create(user_id=request.user.id, nivel_id=nivel + 1, desafio_id=29,
                                                 is_resuelto=False)
                    elif user.xp >= 1500 and len(list_nivel) >= 5 and nivel == 3:
                        UserNivel.objects.create(user_id=request.user.id, nivel_id=nivel + 1, desafio_id=34,
                                                 is_resuelto=False)
                    else:
                        UserNivel.objects.create(user_id=request.user.id, nivel_id=nivel, desafio_id=desafio + 1,
                                                 is_resuelto=False)

                desafio_actual.save()
                user.save()

            return Response({
                'resultado': resultado
            }, status=status.HTTP_200_OK)
        else:
            return Response({
                'message': 'No tienes suficiente energia para realizar esta acción'
            }, status=status.HTTP_423_LOCKED)
