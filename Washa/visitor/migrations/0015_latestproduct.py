# Generated by Django 3.1.4 on 2021-02-10 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visitor', '0014_auto_20210210_1141'),
    ]

    operations = [
        migrations.CreateModel(
            name='LatestProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(max_length=50)),
                ('img', models.ImageField(upload_to='latest_img/')),
                ('P_name', models.CharField(max_length=50)),
                ('P_price', models.CharField(max_length=10)),
            ],
        ),
    ]
