# Generated by Django 3.1.4 on 2021-03-01 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userProfileApp', '0004_auto_20210301_2046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='allregister',
            name='userConPass',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='allregister',
            name='userMail',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='allregister',
            name='userPass',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]