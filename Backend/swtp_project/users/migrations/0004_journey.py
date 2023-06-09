# Generated by Django 4.0.8 on 2022-10-27 14:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_car_user_cars_owned'),
    ]

    operations = [
        migrations.CreateModel(
            name='Journey',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('distance_miles', models.DecimalField(decimal_places=2, max_digits=7)),
                ('energy_used_kwh', models.DecimalField(decimal_places=2, max_digits=7)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('start_battery_percent', models.DecimalField(decimal_places=2, max_digits=6)),
                ('end_battery_percent', models.DecimalField(decimal_places=2, max_digits=6)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.car')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
