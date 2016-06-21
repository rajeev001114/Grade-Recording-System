# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TCH', '0005_auto_20150929_1338'),
        ('ADM', '0010_auto_20150926_1332'),
        ('MSG', '0034_student_marks'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bm_max_marks',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('course_name', models.CharField(max_length=50)),
                ('all_eval', models.TextField(null=True)),
                ('max_marks', models.TextField(null=True)),
                ('personid', models.ForeignKey(to='TCH.Personinformation')),
                ('sessionid', models.ForeignKey(to='ADM.Academic_session')),
            ],
        ),
        migrations.CreateModel(
            name='Bm_student_marks',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('course_name', models.CharField(max_length=50)),
                ('marks', models.TextField(null=True)),
                ('personid', models.ForeignKey(to='TCH.Personinformation')),
                ('sessionid', models.ForeignKey(to='ADM.Academic_session')),
            ],
        ),
    ]
