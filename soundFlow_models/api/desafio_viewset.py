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

    @action(detail=True, methods=['GET'], url_path='get-desafio-level', url_name='Obtener desafio por nivel', permission_classes=[IsAuthenticated])
    def get_desafio_level(self, request, pk=None):
        if pk is None:
            return Response({'message': 'El nivel no existe'}, status=404)
        try:
            desafio = Desafio.objects.filter(nivel_id=pk)
            return Response(DesafioSerializer(desafio, many=True).data)
        except Desafio.DoesNotExist:
            return Response({'message': 'El desafio no existe'}, status=404)

    @action(detail=True, methods=['GET'], url_path='get_desafios_habilitados_user',
            url_name='Obtener desafios habilitados por usuario', permission_classes=[IsAuthenticated])
    def get_desafios_habilitados_user(self, request, pk=None):
        desafio_user = [desafio['desafio_id'] for desafio in
                        UserNivel.objects.filter(user_id=request.user.id).values('desafio_id')]
        print(desafio_user)
        desafios = Desafio.objects.filter(nivel_id=pk)
        desafios_habilitados = [desafios for desafios in desafios if desafios.id in desafio_user]
        return Response(DesafioSerializer(desafios_habilitados, many=True).data)
