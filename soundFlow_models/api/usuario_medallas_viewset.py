from rest_framework import serializers, viewsets

from soundFlow_models.models import UsuarioMedallas


class UsuarioMedallasSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsuarioMedallas
        fields = '__all__'


class UsuarioMedallasViewSet(viewsets.ModelViewSet):
    queryset = UsuarioMedallas.objects.all()
    serializer_class = UsuarioMedallasSerializer
