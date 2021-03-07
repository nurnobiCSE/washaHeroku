# Generated by Django 3.1.4 on 2021-02-16 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact_apps', '0002_contact_banner'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact_address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(max_length=50)),
                ('details', models.TextField(max_length=250)),
                ('location', models.CharField(max_length=250)),
                ('mobile', models.CharField(max_length=50)),
                ('mobile2', models.CharField(max_length=50)),
                ('mail', models.CharField(max_length=50)),
                ('website', models.CharField(max_length=50)),
                ('website2', models.CharField(max_length=50)),
            ],
        ),
    ]
