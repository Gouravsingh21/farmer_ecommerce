# Generated by Django 3.1.4 on 2021-01-14 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Food', '0007_auto_20210114_2251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_acct',
            name='mobile',
            field=models.IntegerField(null=True),
        ),
    ]