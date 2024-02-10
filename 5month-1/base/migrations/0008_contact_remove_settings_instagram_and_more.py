# Generated by Django 5.0.1 on 2024-02-07 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_galery_link'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instagram', models.URLField(blank=True, null=True, verbose_name='Ссылка на инстаграм')),
                ('youtube', models.URLField(blank=True, null=True, verbose_name='Ссылка на ютуб')),
                ('telegram', models.URLField(blank=True, null=True, verbose_name='Ссылка на телеграм')),
                ('phone_1', models.CharField(blank=True, max_length=25, null=True, verbose_name='Телефон 1')),
                ('phone_2', models.CharField(blank=True, max_length=25, null=True, verbose_name='Телефон 2')),
                ('email_1', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email 1')),
                ('email_2', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email 2')),
                ('address', models.CharField(blank=True, max_length=100, null=True, verbose_name='Адрес')),
            ],
        ),
        migrations.RemoveField(
            model_name='settings',
            name='instagram',
        ),
        migrations.RemoveField(
            model_name='settings',
            name='telegram',
        ),
        migrations.RemoveField(
            model_name='settings',
            name='youtube',
        ),
    ]
