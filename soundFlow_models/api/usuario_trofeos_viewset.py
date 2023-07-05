from rest_framework import serializers, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from soundFlow_models.api import TrofeoSerializer
from soundFlow_models.models import UsuarioTrofeos, Trofeo


class UsuarioTrofeosSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsuarioTrofeos
        fields = '__all__'


class UsuarioTrofeosViewSet(viewsets.ModelViewSet):
    queryset = UsuarioTrofeos.objects.all()
    serializer_class = UsuarioTrofeosSerializer

    @action(detail=False, methods=['GET'], url_path='get-trofeos-by-user', url_name='Obtener trofeos por usuario', permission_classes=[IsAuthenticated])
    def get_trofeos_by_user(self, request):
        trofeos_user = UsuarioTrofeos.objects.filter(user_id=request.user.id).values('trofeo_id')
        trofeos = Trofeo.objects.filter(id__in=trofeos_user)
        return Response(TrofeoSerializer(trofeos, many=True).data)
