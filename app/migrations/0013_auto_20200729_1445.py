# Generated by Django 2.0 on 2020-07-29 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_auto_20200710_1041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crimes_against_women',
            name='Area_Name',
            field=models.CharField(max_length=1400),
        ),
        migrations.AlterField(
            model_name='murder',
            name='Area_Name',
            field=models.CharField(max_length=1400),
        ),
    ]
