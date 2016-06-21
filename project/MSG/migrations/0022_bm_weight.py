# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MSG', '0021_remove_student_marks_gp_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bm_weight',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('teacher_id', models.IntegerField()),
                ('course_id', models.CharField(max_length=45)),
                ('bmoocs_weight', models.IntegerField()),
            ],
        ),
    ]
