# Generated by Django 2.0 on 2020-05-14 07:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crimefiles', '0039_auto_20200514_1204'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='caseclose',
            options={'verbose_name': 'crimefilesdata', 'verbose_name_plural': 'crimefilesdata'},
        ),
        migrations.AlterModelOptions(
            name='casestatus',
            options={'verbose_name': 'crimefilesdata', 'verbose_name_plural': 'crimefilesdata'},
        ),
        migrations.AlterModelOptions(
            name='complaint',
            options={'verbose_name': 'crimefilesdata', 'verbose_name_plural': 'crimefilesdata'},
        ),
        migrations.AlterModelOptions(
            name='copstatus',
            options={'verbose_name': 'crimefilesdata', 'verbose_name_plural': 'crimefilesdata'},
        ),
        migrations.AlterModelOptions(
            name='fir',
            options={'verbose_name': 'crimefilesdata', 'verbose_name_plural': 'crimefilesdata'},
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
            model_name='fir',
            name='complaintid',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='crimefiles.Complaint'),
        ),
    ]