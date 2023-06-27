from rest_framework import viewsets, serializers

from soundFlow_models.models import Medalla


class MedallaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medalla
        fields = '__all__'


class MedallaViewSet(viewsets.ModelViewSet):
    queryset = Medalla.objects.all()
    serializer_class = MedallaSerializer
