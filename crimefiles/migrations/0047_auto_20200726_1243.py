# Generated by Django 2.0 on 2020-07-26 07:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crimefiles', '0046_auto_20200726_1125'),
    ]

    operations = [
        migrations.AddField(
            model_name='complaint',
            name='complaint_registered',
            field=models.BooleanField(default=False, max_length=100),
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
            model_name='freport',
            name='complaintid',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='crimefiles.Complaint'),
        ),
    ]
