# Generated by Django 2.0 on 2020-07-13 05:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crimefiles', '0061_auto_20200712_1140'),
    ]

    operations = [
        migrations.CreateModel(
            name='freport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facilitatorviews', models.CharField(blank=True, default='', max_length=2000, null=True)),
                ('facilitator_statement', models.FileField(blank=True, default='', max_length=1000, null=True, upload_to='fstatements/')),
                ('f_evidence1', models.FileField(blank=True, default='', max_length=1000, null=True, upload_to='f_evidences/')),
                ('f_evidence2', models.FileField(blank=True, default='', max_length=1000, null=True, upload_to='f_evidences/')),
                ('f_evidence3', models.FileField(blank=True, default='', max_length=1000, null=True, upload_to='f_evidences/')),
            ],
        ),
        migrations.RemoveField(
            model_name='complaint',
            name='f_evidence1',
        ),
        migrations.RemoveField(
            model_name='complaint',
            name='f_evidence2',
        ),
        migrations.RemoveField(
            model_name='complaint',
            name='f_evidence3',
        ),
        migrations.RemoveField(
            model_name='complaint',
            name='facilitator_statement',
        ),
        migrations.RemoveField(
            model_name='complaint',
            name='facilitatorviews',
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
        migrations.AddField(
            model_name='freport',
            name='complaintid',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='crimefiles.Complaint'),
        ),
    ]
