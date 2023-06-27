from rest_framework import serializers, viewsets

from soundFlow_models.models import Audio


class AudioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Audio
        fields = '__all__'


class AudioViewSet(viewsets.ModelViewSet):
    queryset = Audio.objects.all()
    serializer_class = AudioSerializer
