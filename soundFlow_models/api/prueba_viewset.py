from rest_framework import viewsets, serializers

from soundFlow_models.models import Prueba


class PruebaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prueba
        fields = '__all__'


class PruebaViewSet(viewsets.ModelViewSet):
    queryset = Prueba.objects.all()
    serializer_class = PruebaSerializer
