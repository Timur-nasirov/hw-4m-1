from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import AllowAny, IsAuthenticated

from apps.coins.serializers import CoinSerializer
from apps.users.models import User
from apps.users.permissions import UserPermissions

class CoinAPIViewSet(
    GenericViewSet,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin
):
    queryset = User.objects.all()
    serializer_class = CoinSerializer
    permission_classes = IsAuthenticated
    
    def get_permissions(self):
        if self.action in ('list', 'update', 'partial_update'):
            return (UserPermissions(), )
        return (AllowAny(), )

