# Generated by Django 2.0 on 2020-07-10 15:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crimefiles', '0050_auto_20200710_1748'),
    ]

    operations = [
        migrations.AddField(
            model_name='complaint',
            name='csignstatus',
            field=models.CharField(choices=[('Csign Added', 'Csign Added'), ('Csign Not Added', 'Csign Not Added')], default='Csign Not Added', max_length=25),
        ),
        migrations.AddField(
            model_name='complaint',
            name='sketchstatus',
            field=models.CharField(choices=[('Criminal Sketch Added', 'Criminal Sketch Added'), ('Criminal Sketch Not Added', 'Criminal Sketch Not Added'), ('Criminal Sketch Skipped', 'Criminal Sketch Skipped')], default='Criminal Sketch Not Added', max_length=50),
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