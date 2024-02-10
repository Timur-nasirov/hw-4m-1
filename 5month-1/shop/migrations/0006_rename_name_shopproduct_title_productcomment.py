# Generated by Django 5.0.1 on 2024-02-09 16:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_menu'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shopproduct',
            old_name='name',
            new_name='title',
        ),
        migrations.CreateModel(
            name='ProductComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Имя')),
                ('content', models.TextField(verbose_name='Содержание')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.shopproduct', verbose_name='Продукт')),
            ],
            options={
                'verbose_name': 'Коментраий к продукту',
                'verbose_name_plural': 'Комментарии к продуктами',
            },
        ),
    ]