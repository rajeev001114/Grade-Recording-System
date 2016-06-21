# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TCH', '0004_courseallotment_is_active'),
        ('ADM', '0010_auto_20150926_1332'),
        ('MSG', '0027_auto_20150927_0910'),
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('file', models.FileField(upload_to=b'.')),
            ],
        ),
        migrations.CreateModel(
            name='Grade_policy',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('gp_id', models.CharField(max_length=50)),
                ('abbreviation', models.CharField(max_length=4)),
                ('assignment', models.CharField(max_length=20)),
                ('total', models.IntegerField()),
                ('mandatory', models.IntegerField()),
                ('weight', models.IntegerField()),
                ('consolidated', models.CharField(max_length=1)),
                ('seq_number', models.IntegerField()),
                ('course_code', models.CharField(max_length=45)),
                ('personid', models.ForeignKey(to='TCH.Personinformation')),
                ('sessionid', models.ForeignKey(to='ADM.Academic_session')),
            ],
        ),
    ]
