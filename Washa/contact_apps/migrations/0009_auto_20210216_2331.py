# Generated by Django 3.1.4 on 2021-02-16 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact_apps', '0008_auto_20210216_2330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='msgbox',
            name='f_name',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
    ]
