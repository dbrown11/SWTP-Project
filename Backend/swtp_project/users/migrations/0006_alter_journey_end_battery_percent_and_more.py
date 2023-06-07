# Generated by Django 4.0.8 on 2022-10-27 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_journey_end_battery_percent_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journey',
            name='end_battery_percent',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
        migrations.AlterField(
            model_name='journey',
            name='start_battery_percent',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
    ]