# Generated by Django 3.1.3 on 2021-04-24 02:04

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('login', '0006_auto_20210424_0643'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Profile',
            new_name='Profile1',
        ),
    ]
