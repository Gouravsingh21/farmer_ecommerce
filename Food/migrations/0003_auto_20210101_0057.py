# Generated by Django 3.1.4 on 2020-12-31 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Food', '0002_auto_20201231_1229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='Date',
            field=models.DateField(auto_now=True),
        ),
    ]