from rest_framework import serializers, viewsets

from soundFlow_models.models import Imagen


class ImagenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Imagen
        fields = '__all__'


class ImagenViewSet(viewsets.ModelViewSet):
    queryset = Imagen.objects.all()
    serializer_class = ImagenSerializer
