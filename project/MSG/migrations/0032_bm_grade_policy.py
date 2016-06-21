# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TCH', '0005_auto_20150929_1338'),
        ('ADM', '0010_auto_20150926_1332'),
        ('MSG', '0031_bm_weight_course_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bm_grade_policy',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('course_name', models.CharField(max_length=50)),
                ('min_count', models.IntegerField()),
                ('weight', models.FloatField(default=0)),
                ('examtype', models.CharField(max_length=50)),
                ('drop_count', models.IntegerField()),
                ('short_label', models.CharField(max_length=20)),
                ('personid', models.ForeignKey(to='TCH.Personinformation')),
                ('sessionid', models.ForeignKey(to='ADM.Academic_session')),
            ],
        ),
    ]
