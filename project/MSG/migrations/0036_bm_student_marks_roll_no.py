# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MSG', '0035_bm_max_marks_bm_student_marks'),
    ]

    operations = [
        migrations.AddField(
            model_name='bm_student_marks',
            name='roll_no',
            field=models.CharField(default=b'0', max_length=30),
        ),
    ]
