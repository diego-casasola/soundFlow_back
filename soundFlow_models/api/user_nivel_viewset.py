from rest_framework import viewsets, serializers

from soundFlow_models.models import UserNivel


class UserNivelSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserNivel
        fields = '__all__'


class UserNivelViewSet(viewsets.ModelViewSet):
    queryset = UserNivel.objects.all()
    serializer_class = UserNivelSerializer
