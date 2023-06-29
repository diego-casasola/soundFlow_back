from rest_framework import viewsets, serializers
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from soundFlow_models.models import Desafio, UserNivel


class DesafioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Desafio
        fields = '__all__'


class DesafioViewSet(viewsets.ModelViewSet):
    queryset = Desafio.objects.all()
    serializer_class = DesafioSerializer

    @action(detail=False, methods=['GET'], url_path='get_desafios_habilitados_user',
            url_name='Obtener desafios habilitados por usuario', permission_classes=[IsAuthenticated])
    def get_desafios_habilitados_user(self, request):
        nivel = request.data['nivel']
        desafio_user = [desafio['desafio_id'] for desafio in
                        UserNivel.objects.filter(user_id=request.user.id).values('desafio_id')]
        desafios = Desafio.objects.filter(nivel_id=nivel)
        desafios_habilitados = [desafios for desafios in desafios if desafios.id in desafio_user]
        return Response(DesafioSerializer(desafios_habilitados, many=True).data)
