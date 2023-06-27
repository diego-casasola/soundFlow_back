from rest_framework import serializers, viewsets

from soundFlow_models.models import Nivel


class NivelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nivel
        fields = '__all__'


class NivelViewSet(viewsets.ModelViewSet):
    queryset = Nivel.objects.all()
    serializer_class = NivelSerializer
