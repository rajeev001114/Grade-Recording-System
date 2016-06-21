# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MSG', '0026_auto_20150920_1403'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Bm_weight',
        ),
        migrations.DeleteModel(
            name='Content',
        ),
        migrations.DeleteModel(
            name='CourseGrade',
        ),
        migrations.DeleteModel(
            name='ErrorContent',
        ),
        migrations.DeleteModel(
            name='Grade_policy',
        ),
        migrations.DeleteModel(
            name='Max_marks',
        ),
        migrations.DeleteModel(
            name='Policy_weight',
        ),
        migrations.DeleteModel(
            name='Student_marks',
        ),
    ]
