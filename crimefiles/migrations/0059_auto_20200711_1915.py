# Generated by Django 2.0 on 2020-07-11 13:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crimefiles', '0058_auto_20200711_1856'),
    ]

    operations = [
        migrations.AddField(
            model_name='facilitator_details',
            name='fimage',
            field=models.ImageField(blank=True, default='', null=True, upload_to='fimages/'),
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