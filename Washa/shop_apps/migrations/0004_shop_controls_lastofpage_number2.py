# Generated by Django 3.1.4 on 2021-02-14 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_apps', '0003_auto_20210213_2246'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop_controls',
            name='lastOfPage_number2',
            field=models.IntegerField(default=10),
        ),
    ]
