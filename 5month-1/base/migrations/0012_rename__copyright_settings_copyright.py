# Generated by Django 5.0.1 on 2024-02-07 16:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0011_about'),
    ]

    operations = [
        migrations.RenameField(
            model_name='settings',
            old_name='_copyright',
            new_name='copyright',
        ),
    ]