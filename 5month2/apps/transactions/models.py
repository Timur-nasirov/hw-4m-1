from django.db import models
from apps.users.models import User

# Create your models here.
class Transaction(models.Model):
    from_user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='От кого',
        related_name='from_user'
    )
    to_user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Кому',
        related_name='to_user'
    )
    amount = models.PositiveSmallIntegerField(
        verbose_name='Сумма'
    )
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания'
    )
    
    class Meta:
        verbose_name = 'Транзакция'
        verbose_name_plural = 'Транзакции'
        