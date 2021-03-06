# Generated by Django 3.1.4 on 2021-01-09 06:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Food', '0003_auto_20210101_0057'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_acct',
            fields=[
                ('UserId', models.AutoField(primary_key=True, serialize=False)),
                ('Username', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=30)),
                ('mobile', models.IntegerField()),
                ('Date', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='User_cart',
            fields=[
                ('cartId', models.AutoField(primary_key=True, serialize=False)),
                ('no_of_product', models.IntegerField()),
                ('product_name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='User_delivery',
            fields=[
                ('deliveryId', models.AutoField(primary_key=True, serialize=False)),
                ('deliverydt', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='User_order',
            fields=[
                ('orderId', models.AutoField(primary_key=True, serialize=False)),
                ('orderdt', models.DateTimeField(auto_now=True)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Food.user_cart')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Food.user_acct')),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.AddField(
            model_name='user_delivery',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Food.user_order'),
        ),
        migrations.AddField(
            model_name='user_delivery',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Food.user_acct'),
        ),
    ]
