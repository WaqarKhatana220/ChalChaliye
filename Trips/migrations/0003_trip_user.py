# Generated by Django 3.1.3 on 2021-04-10 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Trips', '0002_auto_20210410_1944'),
    ]

    operations = [
        migrations.AddField(
            model_name='trip',
            name='user',
            field=models.CharField(max_length=32, null=True),
        ),
    ]
