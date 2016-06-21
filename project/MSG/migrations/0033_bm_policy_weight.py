# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TCH', '0005_auto_20150929_1338'),
        ('ADM', '0010_auto_20150926_1332'),
        ('MSG', '0032_bm_grade_policy'),
    ]

    operations = [
        migrations.CreateModel(
            name='BM_policy_weight',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('course_name', models.CharField(max_length=50)),
                ('pweight', models.TextField()),
                ('personid', models.ForeignKey(to='TCH.Personinformation')),
                ('sessionid', models.ForeignKey(to='ADM.Academic_session')),
            ],
        ),
    ]
