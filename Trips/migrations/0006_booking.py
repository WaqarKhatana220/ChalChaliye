# Generated by Django 3.1.3 on 2021-04-24 17:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Trips', '0005_auto_20210424_0810'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('participent', models.IntegerField()),
                ('trip', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='Trips.trip')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
