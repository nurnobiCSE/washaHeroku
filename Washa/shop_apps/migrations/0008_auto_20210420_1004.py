# Generated by Django 3.1.4 on 2021-04-20 04:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_apps', '0007_shopprduct_product_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopprduct',
            name='product_code',
            field=models.CharField(default='', max_length=50, null=True),
        ),
    ]
