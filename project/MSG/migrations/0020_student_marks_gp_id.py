# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MSG', '0019_max_marks_student_marks'),
    ]

    operations = [
        migrations.AddField(
            model_name='student_marks',
            name='gp_id',
            field=models.CharField(default=23, max_length=50),
            preserve_default=False,
        ),
    ]
