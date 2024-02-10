# Generated by Django 5.0.1 on 2024-02-09 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0021_reservation'),
    ]

    operations = [
        migrations.CreateModel(
            name='Terms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('content', models.TextField(verbose_name='Политика конфиденциальности')),
            ],
            options={
                'verbose_name': 'Политика конфиденциальности',
                'verbose_name_plural': 'Политики конфиденциальности',
            },
        ),
    ]
