from django.urls import include, re_path, path
from rest_framework import routers
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView

from authentication.api import UserViewSet, MyTokenObtainPairViewSet

router = routers.DefaultRouter()
router.register(r'user', UserViewSet)

urlpatterns = [
    re_path(r'^', include(router.urls)),
    path('auth/token/', MyTokenObtainPairViewSet.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]