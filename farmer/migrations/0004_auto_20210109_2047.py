# Generated by Django 3.1.4 on 2021-01-09 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farmer', '0003_auto_20210109_1227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='farmer_info',
            name='mobile',
            field=models.IntegerField(unique=True),
        ),
    ]
