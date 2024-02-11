from django.contrib import admin
from apps.transactions.models import Transaction

# Register your models here.
@admin.register(Transaction)
class AdminTransaction(admin.ModelAdmin):
    list_display = ('from_user', 'to_user', 'amount', 'created')