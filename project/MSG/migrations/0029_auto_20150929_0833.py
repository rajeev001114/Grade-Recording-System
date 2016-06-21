# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ADM', '0010_auto_20150926_1332'),
        ('TCH', '0004_courseallotment_is_active'),
        ('MSG', '0028_content_grade_policy'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseGrade',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('gp_id', models.CharField(max_length=50)),
                ('course_code', models.CharField(max_length=20)),
                ('personid', models.ForeignKey(to='TCH.Personinformation')),
                ('sessionid', models.ForeignKey(to='ADM.Academic_session')),
            ],
        ),
        migrations.RemoveField(
            model_name='grade_policy',
            name='consolidated',
        ),
        migrations.RemoveField(
            model_name='grade_policy',
            name='course_code',
        ),
        migrations.RemoveField(
            model_name='grade_policy',
            name='personid',
        ),
        migrations.RemoveField(
            model_name='grade_policy',
            name='seq_number',
        ),
        migrations.RemoveField(
            model_name='grade_policy',
            name='sessionid',
        ),
    ]
