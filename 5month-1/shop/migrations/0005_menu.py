# Generated by Django 5.0.1 on 2024-02-09 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_rename_shopcheap_shopdish_alter_shopdish_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('description', models.TextField(verbose_name='Описание')),
                ('new_price', models.SmallIntegerField(verbose_name='Новая цена')),
                ('old_price', models.SmallIntegerField(verbose_name='Старая цена')),
            ],
            options={
                'verbose_name': 'Меню',
                'verbose_name_plural': 'Меню',
            },
        ),
    ]