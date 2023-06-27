from rest_framework import viewsets, serializers

from soundFlow_models.models import Desafio


class DesafioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Desafio
        fields = '__all__'


class DesafioViewSet(viewsets.ModelViewSet):
    queryset = Desafio.objects.all()
    serializer_class = DesafioSerializer
