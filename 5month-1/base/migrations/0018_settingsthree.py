# Generated by Django 5.0.1 on 2024-02-08 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0017_settingstwo'),
    ]

    operations = [
        migrations.CreateModel(
            name='SettingsThree',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_1', models.CharField(max_length=255, verbose_name='Заголовок 1')),
                ('desc_1', models.TextField(verbose_name='Описание 1')),
                ('image_1', models.ImageField(upload_to='settings3/banner1/', verbose_name='Баннер 1')),
                ('title_2', models.CharField(max_length=255, verbose_name='Заголовок 2')),
                ('desc_2', models.TextField(verbose_name='Описание 2')),
                ('image_2', models.ImageField(upload_to='settings3/banner2/', verbose_name='Баннер 2')),
                ('customers', models.SmallIntegerField(verbose_name='Количеcтво клиентов')),
                ('outlet', models.SmallIntegerField(verbose_name='Количетсво торговых точек')),
                ('satis', models.SmallIntegerField(verbose_name='Процент удовлетворения клиентов')),
            ],
            options={
                'verbose_name': 'Настройка третей главной страницы',
                'verbose_name_plural': 'Настройки третей главной страницы',
            },
        ),
    ]