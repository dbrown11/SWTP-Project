# Generated by Django 4.0.8 on 2022-11-04 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_journey_end_battery_percent_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='journey',
            name='data',
            field=models.JSONField(null=True),
        ),
    ]
