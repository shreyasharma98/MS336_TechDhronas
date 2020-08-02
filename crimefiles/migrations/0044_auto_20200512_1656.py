# Generated by Django 2.0 on 2020-05-12 11:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crimefiles', '0043_auto_20200512_1638'),
    ]

    operations = [
        migrations.AddField(
            model_name='fir',
            name='decline_reason_police',
            field=models.CharField(blank=True, default='No Reason', max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='fir',
            name='decline_reason_sho',
            field=models.CharField(blank=True, default='No Reason', max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='fir',
            name='decline_reason_sp',
            field=models.CharField(blank=True, default='No Reason', max_length=1000, null=True),
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
        migrations.AlterField(
            model_name='reason',
            name='complaintid',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='crimefiles.Complaint'),
        ),
    ]
