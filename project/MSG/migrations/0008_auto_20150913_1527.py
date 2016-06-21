# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MSG', '0007_auto_20150913_1439'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CourseGrade',
        ),
        migrations.DeleteModel(
            name='ErrorContent',
        ),
        migrations.DeleteModel(
            name='Grade_policy',
        ),
    ]
