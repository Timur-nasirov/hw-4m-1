from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.routers import DefaultRouter

from apps.users.views import UserAPIViewSet

router = DefaultRouter()
router.register('user', UserAPIViewSet, 'api_users')

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='api_users_login'),
    path('refresh/', TokenRefreshView.as_view(), name='api_users_refresh')
]

urlpatterns += router.urls