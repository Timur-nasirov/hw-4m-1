from rest_framework.routers import DefaultRouter
from apps.coins.views import *

router = DefaultRouter()
router.register('coin', CoinAPIViewSet, 'api_coins')

urlpatterns = router.urls