# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MSG', '0036_bm_student_marks_roll_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bm_max_marks',
            name='all_eval',
            field=models.CharField(default=2, max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='bm_max_marks',
            name='max_marks',
            field=models.IntegerField(),
        ),
    ]
