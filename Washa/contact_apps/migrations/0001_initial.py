# Generated by Django 3.1.4 on 2021-02-16 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Header_footerData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_title', models.CharField(max_length=50)),
                ('number', models.CharField(max_length=15)),
                ('logo', models.ImageField(upload_to='logoimage/')),
                ('footerLogo_describ', models.TextField(default='', max_length=500)),
                ('footerLogo_describ_2', models.TextField(default='', max_length=500)),
                ('footerContact_header', models.CharField(default='', max_length=50)),
                ('footerContact_location', models.CharField(default='', max_length=200)),
                ('footerContact_telePhone', models.CharField(default='', max_length=50)),
                ('footerContact_mail', models.CharField(default='', max_length=50)),
                ('footerContact_webSite', models.CharField(default='', max_length=70)),
                ('copyRight', models.CharField(default='', max_length=50)),
                ('copyRightBy', models.CharField(default='', max_length=50)),
            ],
        ),
    ]
