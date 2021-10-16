# Generated by Django 3.1.4 on 2021-02-09 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visitor', '0009_shipping_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='special_part',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='special_images/')),
                ('product_head', models.CharField(max_length=50)),
                ('product_name', models.CharField(max_length=250)),
                ('button_name', models.CharField(max_length=50)),
            ],
        ),
    ]