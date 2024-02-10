# Generated by Django 5.0.1 on 2024-02-08 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0015_helpmessage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Faq',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_1', models.CharField(max_length=255, verbose_name='Заголовок 1')),
                ('desc_1', models.TextField(verbose_name='Описание 1')),
                ('title_2', models.CharField(max_length=255, verbose_name='Заголовок 2')),
                ('desc_2', models.TextField(verbose_name='Описание 2')),
                ('title_3', models.CharField(max_length=255, verbose_name='Заголовок 3')),
                ('desc_3', models.TextField(verbose_name='Описание 3')),
                ('title_4', models.CharField(max_length=255, verbose_name='Заголовок 4')),
                ('desc_4', models.TextField(verbose_name='Описание 4')),
                ('title_5', models.CharField(max_length=255, verbose_name='Заголовок 5')),
                ('desc_5', models.TextField(verbose_name='Описание 5')),
            ],
            options={
                'verbose_name': 'Настройка FAQ',
                'verbose_name_plural': 'Настройки FAQ',
            },
        ),
    ]