# Generated by Django 2.0 on 2020-07-29 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wanted', '0002_auto_20200729_1735'),
    ]

    operations = [
        migrations.CreateModel(
            name='user_criminal_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_informer', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('name_of_criminal', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('date', models.DateField(auto_now_add=True)),
                ('info', models.TextField(blank=True, default='', max_length=1000, null=True)),
                ('info_image', models.ImageField(blank=True, default='', null=True, upload_to='useraddedcinfo/')),
            ],
        ),
    ]
