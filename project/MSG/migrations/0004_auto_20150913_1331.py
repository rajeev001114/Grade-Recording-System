# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MSG', '0003_auto_20150913_1323'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ErrorContent',
        ),
        migrations.RemoveField(
            model_name='grade_policy',
            name='gp_id',
        ),
        migrations.DeleteModel(
            name='CourseGrade',
        ),
        migrations.DeleteModel(
            name='Grade_policy',
        ),
    ]
