from django.urls import re_path, include
from rest_framework import routers

from soundFlow_models.api import *

router = routers.DefaultRouter()
router.register(r'prueba', PruebaViewSet)
router.register(r'trofeo', TrofeoViewSet)
router.register(r'desafio', DesafioViewSet)
router.register(r'nivel', NivelViewSet)
router.register(r'medalla', MedallaViewSet)
router.register(r'audio', AudioViewSet)
router.register(r'imagen', ImagenViewSet)
router.register(r'user_nivel', UserNivelViewSet)
router.register(r'usuario_trofeos', UsuarioTrofeosViewSet)
router.register(r'usuario_medallas', UsuarioMedallasViewSet)

urlpatterns = [
    re_path(r'^', include(router.urls)),
]