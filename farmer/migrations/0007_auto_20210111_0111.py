# Generated by Django 3.1.4 on 2021-01-10 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farmer', '0006_farmer_product_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='farmer_product',
            name='product_image',
            field=models.ImageField(default='', upload_to='media/farmer/images'),
        ),
    ]
