# Generated by Django 3.1.4 on 2021-03-01 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userProfileApp', '0002_bannarlayout_formlayout'),
    ]

    operations = [
        migrations.CreateModel(
            name='allRegister',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userName', models.CharField(max_length=50)),
                ('userMail', models.CharField(max_length=50)),
                ('userPass', models.CharField(max_length=50)),
                ('userConPass', models.CharField(max_length=50)),
            ],
        ),
    ]
