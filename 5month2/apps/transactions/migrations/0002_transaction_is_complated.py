# Generated by Django 5.0 on 2024-02-11 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='is_complated',
            field=models.BooleanField(default=False, verbose_name='Подтверждение транзакции'),
        ),
    ]