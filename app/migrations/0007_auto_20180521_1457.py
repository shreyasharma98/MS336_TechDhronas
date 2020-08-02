# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-05-21 09:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20180518_1550'),
    ]

    operations = [
        migrations.CreateModel(
            name='murder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Area_Name', models.CharField(max_length=140)),
                ('Year', models.IntegerField()),
                ('Group_Name', models.CharField(max_length=140)),
                ('Victims_Above_50_Yrs', models.IntegerField(null=True)),
                ('Victims_Total', models.IntegerField(null=True)),
                ('Victims_Between_10to14_Yrs', models.IntegerField(null=True)),
                ('Victims_Between_14to18_Yrs', models.IntegerField(null=True)),
                ('Victims_Between_18to30_Yrs', models.IntegerField(null=True)),
                ('Victims_Between_30to50_Yrs', models.IntegerField(null=True)),
                ('Victims_of_Rape_Total', models.IntegerField(null=True)),
                ('Victims_Upto_10_Yrs', models.IntegerField(null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='crimes_against_women',
            name='Year',
            field=models.IntegerField(),
        ),
    ]