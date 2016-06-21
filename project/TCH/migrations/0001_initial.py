# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ADM', '0007_auto_20150924_1920'),
    ]

    operations = [
        migrations.CreateModel(
            name='Courseallotment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('roleid', models.IntegerField()),
                ('startdate', models.DateField()),
                ('enddate', models.DateField()),
                ('courseid', models.ForeignKey(to='ADM.All_course')),
            ],
        ),
        migrations.CreateModel(
            name='Personinformation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.EmailField(max_length=100)),
                ('titleid', models.IntegerField(null=True)),
                ('firstname', models.CharField(max_length=45, null=True)),
                ('lastname', models.CharField(max_length=45, null=True)),
                ('designation', models.IntegerField(null=True)),
                ('gender', models.CharField(max_length=10, null=b'TRUE', choices=[(b'MALE', b'Male'), (b'FEMALE', b'Female'), (b'OTHER', b'OTHER')])),
                ('streamid', models.IntegerField(null=True)),
                ('experience', models.CharField(max_length=45, null=True)),
                ('qualification', models.CharField(max_length=45, null=True)),
                ('telephone1', models.CharField(default=0, max_length=12)),
                ('telephone2', models.CharField(default=0, max_length=12, null=True)),
                ('createdondate', models.DateField(default=django.utils.timezone.now)),
                ('isactive', models.BooleanField(default=1)),
            ],
        ),
        migrations.AddField(
            model_name='courseallotment',
            name='personid',
            field=models.ForeignKey(to='TCH.Personinformation'),
        ),
    ]
