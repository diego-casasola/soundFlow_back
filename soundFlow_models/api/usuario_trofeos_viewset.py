from rest_framework import serializers, viewsets

from soundFlow_models.models import UsuarioTrofeos


class UsuarioTrofeosSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsuarioTrofeos
        fields = '__all__'


class UsuarioTrofeosViewSet(viewsets.ModelViewSet):
    queryset = UsuarioTrofeos.objects.all()
    serializer_class = UsuarioTrofeosSerializer
