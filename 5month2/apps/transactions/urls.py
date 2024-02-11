from rest_framework.routers import DefaultRouter
from apps.transactions.views import TransactionsAPIViews

router = DefaultRouter()
router.register('transaction', TransactionsAPIViews, 'api_transaction')

urlpatterns = router.urls