# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MSG', '0008_auto_20150913_1527'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseGrade',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('teacher_id', models.IntegerField()),
                ('gp_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ErrorContent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('systype', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=100)),
                ('errorcode', models.CharField(default=b'null', unique=True, max_length=20)),
                ('error_message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Grade_policy',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('gp_id', models.IntegerField()),
                ('abbreviation', models.CharField(max_length=4)),
                ('assignment', models.CharField(max_length=20)),
                ('total', models.IntegerField()),
                ('mandatory', models.IntegerField()),
                ('weight', models.IntegerField()),
                ('consolidated', models.CharField(max_length=1)),
                ('seq_number', models.IntegerField()),
            ],
        ),
    ]
