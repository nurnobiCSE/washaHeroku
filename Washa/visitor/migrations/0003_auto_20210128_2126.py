# Generated by Django 3.1.4 on 2021-01-28 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visitor', '0002_auto_20210128_2103'),
    ]

    operations = [
        migrations.AddField(
            model_name='header_footerdata',
            name='footerContact_header',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='header_footerdata',
            name='footerContact_location',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='header_footerdata',
            name='footerContact_mail',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='header_footerdata',
            name='footerContact_telePhone',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='header_footerdata',
            name='footerContact_webSite',
            field=models.CharField(default='', max_length=70),
        ),
        migrations.AddField(
            model_name='header_footerdata',
            name='footerLogo_describ',
            field=models.TextField(default='', max_length=500),
        ),
    ]
