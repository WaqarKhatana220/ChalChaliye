# Generated by Django 3.1.3 on 2021-04-23 01:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_auto_20210423_0256'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='country',
        ),
        migrations.AddField(
            model_name='profile',
            name='address',
            field=models.CharField(max_length=500, null=True),
        ),
    ]