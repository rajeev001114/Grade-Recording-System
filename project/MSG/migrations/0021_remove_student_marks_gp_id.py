# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MSG', '0020_student_marks_gp_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student_marks',
            name='gp_id',
        ),
    ]
