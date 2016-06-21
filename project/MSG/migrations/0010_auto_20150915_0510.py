# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MSG', '0009_coursegrade_errorcontent_grade_policy'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursegrade',
            name='course_id',
            field=models.CharField(default=23, max_length=25),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='coursegrade',
            name='gp_id',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='grade_policy',
            name='gp_id',
            field=models.CharField(max_length=30),
        ),
    ]
