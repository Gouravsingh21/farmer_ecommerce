# Generated by Django 3.1.4 on 2021-02-02 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Food', '0008_auto_20210114_2253'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_order',
            name='price',
            field=models.IntegerField(null=True),
        ),
        migrations.RemoveField(
            model_name='user_order',
            name='cart',
        ),
        migrations.AddField(
            model_name='user_order',
            name='cart',
            field=models.ManyToManyField(to='Food.User_cart'),
        ),
    ]