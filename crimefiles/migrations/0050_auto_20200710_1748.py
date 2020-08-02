# Generated by Django 2.0 on 2020-07-10 12:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crimefiles', '0049_auto_20200528_2027'),
    ]

    operations = [
        migrations.CreateModel(
            name='DummyAadharData',
            fields=[
                ('person_id', models.AutoField(primary_key=True, serialize=False)),
                ('firt_name', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('last_name', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('date_of_birth', models.DateField()),
                ('sex', models.CharField(blank=True, default='', max_length=10, null=True)),
                ('address', models.CharField(blank=True, default='', max_length=500, null=True)),
                ('mobile', models.BigIntegerField(blank=True, default=0, null=True)),
                ('aadhar_no', models.CharField(blank=True, default='', max_length=12, null=True, unique=True)),
                ('email_id', models.EmailField(blank=True, default='', max_length=254, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='caseclose',
            name='complaintid',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='crimefiles.Complaint'),
        ),
        migrations.AlterField(
            model_name='casestatus',
            name='complaintid',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='crimefiles.Complaint'),
        ),
        migrations.AlterField(
            model_name='copstatus',
            name='complaintid',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='crimefiles.Complaint'),
        ),
        migrations.AlterField(
            model_name='declinereason',
            name='complaintid',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='crimefiles.Complaint'),
        ),
        migrations.AlterField(
            model_name='fir',
            name='complaintid',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='crimefiles.Complaint'),
        ),
    ]