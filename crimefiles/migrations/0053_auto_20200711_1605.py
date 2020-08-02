# Generated by Django 2.0 on 2020-07-11 10:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crimefiles', '0052_auto_20200710_2154'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='complaint',
            name='briefofoffence',
        ),
        migrations.RemoveField(
            model_name='complaint',
            name='content',
        ),
        migrations.RemoveField(
            model_name='complaint',
            name='decline_reason_police',
        ),
        migrations.RemoveField(
            model_name='complaint',
            name='decline_reason_sho',
        ),
        migrations.RemoveField(
            model_name='complaint',
            name='decline_reason_sp',
        ),
        migrations.RemoveField(
            model_name='complaint',
            name='digitalsignature',
        ),
        migrations.RemoveField(
            model_name='complaint',
            name='location',
        ),
        migrations.RemoveField(
            model_name='complaint',
            name='nameofcriminal',
        ),
        migrations.RemoveField(
            model_name='complaint',
            name='policestation',
        ),
        migrations.RemoveField(
            model_name='complaint',
            name='residenceofcomplainant',
        ),
        migrations.RemoveField(
            model_name='complaint',
            name='residenceofcriminal',
        ),
        migrations.AddField(
            model_name='complaint',
            name='addressofcomplainant',
            field=models.CharField(blank=True, default='', max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='complaint',
            name='addressofsuspect',
            field=models.CharField(blank=True, default='', max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='complaint',
            name='datetimeofcrime',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='complaint',
            name='descriptionofcrime',
            field=models.CharField(blank=True, default='', max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='complaint',
            name='detailsofsuspect',
            field=models.CharField(blank=True, default='', max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='complaint',
            name='f_evidence1',
            field=models.FileField(blank=True, default='', max_length=1000, null=True, upload_to='f_evidences/'),
        ),
        migrations.AddField(
            model_name='complaint',
            name='f_evidence2',
            field=models.FileField(blank=True, default='', max_length=1000, null=True, upload_to='f_evidences/'),
        ),
        migrations.AddField(
            model_name='complaint',
            name='f_evidence3',
            field=models.FileField(blank=True, default='', max_length=1000, null=True, upload_to='f_evidences/'),
        ),
        migrations.AddField(
            model_name='complaint',
            name='facilitator_statement',
            field=models.FileField(blank=True, default='', max_length=1000, null=True, upload_to='fstatements/'),
        ),
        migrations.AddField(
            model_name='complaint',
            name='facilitatorviews',
            field=models.CharField(blank=True, default='', max_length=2000, null=True),
        ),
        migrations.AddField(
            model_name='complaint',
            name='locationofcomplainantsign',
            field=models.CharField(blank=True, default='', max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='complaint',
            name='locationofsketch',
            field=models.CharField(blank=True, default='', max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='complaint',
            name='nameofsuspect',
            field=models.CharField(blank=True, default='', max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='complaint',
            name='nearestpolicestation',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='complaint',
            name='placeofincidence',
            field=models.CharField(blank=True, default='', max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='complaint',
            name='roleofcomplainant',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='complaint',
            name='typeofincidence',
            field=models.CharField(blank=True, default='', max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='complaint',
            name='userstatement',
            field=models.FileField(blank=True, default='', max_length=1000, null=True, upload_to='userstatements/'),
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
