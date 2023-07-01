from rest_framework import serializers, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from soundFlow_models.models import Nivel, UserNivel


class NivelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nivel
        fields = '__all__'


class NivelViewSet(viewsets.ModelViewSet):
    queryset = Nivel.objects.all()
    serializer_class = NivelSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=['GET'], url_path='get_niveles_habilitados_user', url_name='Obtener niveles habilitados por usuario', permission_classes=[IsAuthenticated])
    def get_niveles_habilitados_user(self, request):
        nivel_user = [nivel['nivel_id'] for nivel in UserNivel.objects.filter(user_id=request.user.id).values('nivel_id')]
        niveles = Nivel.objects.all()
        niveles_habilitados = [niveles for niveles in niveles if niveles.id in nivel_user]
        return Response(NivelSerializer(niveles_habilitados, many=True).data)
