from rest_framework import viewsets, serializers

from soundFlow_models.models import Trofeo


class TrofeoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trofeo
        fields = '__all__'


class TrofeoViewSet(viewsets.ModelViewSet):
    queryset = Trofeo.objects.all()
    serializer_class = TrofeoSerializer
