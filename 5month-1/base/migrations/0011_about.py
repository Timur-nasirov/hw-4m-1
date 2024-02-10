# Generated by Django 5.0.1 on 2024-02-07 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0010_error'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_1', models.CharField(max_length=255, verbose_name='Заголовок 1')),
                ('description_1', models.TextField(verbose_name='Описание 1')),
                ('banner_1', models.ImageField(upload_to='about/banner/', verbose_name='Баннер 1')),
                ('title_2', models.CharField(max_length=255, verbose_name='Заголовок 2')),
                ('description_2', models.TextField(verbose_name='Описание 2')),
                ('banner_2', models.ImageField(upload_to='about/banner/', verbose_name='Баннер 2')),
            ],
            options={
                'verbose_name': 'О нас',
                'verbose_name_plural': 'О нас',
            },
        ),
    ]
