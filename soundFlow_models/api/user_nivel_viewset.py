from rest_framework import viewsets, serializers, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from soundFlow_models.models import UserNivel


class UserNivelSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserNivel
        fields = '__all__'


class UserNivelViewSet(viewsets.ModelViewSet):
    queryset = UserNivel.objects.all()
    serializer_class = UserNivelSerializer

    @action(detail=False, methods=['GET'], url_path='get-desafios-user', url_name='Obtener desafios por usuario', permission_classes=[IsAuthenticated])
    def get_desafios_user(self, request):
        desafios_user = [desafio for desafio in UserNivel.objects.filter(user_id=request.user.id, is_resuelto=True).values('nivel_id', 'desafio_id').order_by('nivel_id')]
        return Response({
            'desafios': desafios_user
        }, status=status.HTTP_200_OK)