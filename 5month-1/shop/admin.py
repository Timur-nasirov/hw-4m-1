from django.contrib import admin
from shop.models import *

# Register your models here.

#data
admin.site.register(ShopProduct)
admin.site.register(ShopDish)
admin.site.register(ShopCategory)

#forms
admin.site.register(Pay)
admin.site.register(ProductComment)

#pages
admin.site.register(Menu)