# Generated by Django 5.0.1 on 2024-02-07 12:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_rename_descriprion_shopcheap_descriprtion'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shopcheap',
            old_name='descriprtion',
            new_name='description',
        ),
    ]