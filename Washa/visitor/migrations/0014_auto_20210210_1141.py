# Generated by Django 3.1.4 on 2021-02-10 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visitor', '0013_auto_20210210_1140'),
    ]

    operations = [
        migrations.AddField(
            model_name='newproduct',
            name='day',
            field=models.CharField(default='', max_length=5),
        ),
        migrations.AddField(
            model_name='newproduct',
            name='month',
            field=models.CharField(default='', max_length=5),
        ),
        migrations.AddField(
            model_name='newproduct',
            name='year',
            field=models.CharField(default='', max_length=5),
        ),
    ]
