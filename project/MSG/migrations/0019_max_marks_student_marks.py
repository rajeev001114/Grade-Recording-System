# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MSG', '0018_auto_20150917_0722'),
    ]

    operations = [
        migrations.CreateModel(
            name='Max_marks',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('teacher_id', models.IntegerField()),
                ('gp_id', models.CharField(max_length=50)),
                ('course_id', models.CharField(max_length=45)),
                ('all_eval', models.TextField(null=True)),
                ('max_marks', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Student_marks',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('roll_no', models.CharField(default=b'0', max_length=30)),
                ('marks_obtain', models.TextField(null=True)),
                ('teacher_id', models.IntegerField()),
                ('course_id', models.CharField(max_length=45)),
            ],
        ),
    ]
