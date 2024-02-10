from django.urls import path
from shop.views import * 

urlpatterns = [
    path('<int:id>/', shop_details, name='shop-details'),
    path('cart/', cart, name='cart'),
    path('checkout/', checkout, name='checkout'),
    path('menu/', menu, name='menu'),
    path('', shop, name='shop')
]