# Generated by Django 2.0 on 2020-07-29 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CaseStatus',
            fields=[
                ('criminalid', models.AutoField(primary_key=True, serialize=False)),
                ('criminal_name', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('criminal_image', models.ImageField(blank=True, default='', null=True, upload_to='criminal_images/')),
                ('gender', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('police_station', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('crime_no', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('section_of_law', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('wanted_from_date', models.DateField(blank=True, null=True)),
                ('date_of_birth', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('height', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('build', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('complextion', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('crime_description', models.CharField(blank=True, default='', max_length=1000, null=True)),
                ('address_criminal', models.CharField(blank=True, default='', max_length=500, null=True)),
            ],
        ),
    ]
