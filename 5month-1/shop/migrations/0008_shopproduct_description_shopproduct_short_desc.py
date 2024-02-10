# Generated by Django 5.0.1 on 2024-02-09 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_shopproduct_image_shopproduct_sku_shopproduct_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopproduct',
            name='description',
            field=models.TextField(default=1, verbose_name='Полное описание'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='shopproduct',
            name='short_desc',
            field=models.TextField(default=1, verbose_name='Короткое описание'),
            preserve_default=False,
        ),
    ]