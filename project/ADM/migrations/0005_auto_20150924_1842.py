# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ADM', '0004_auto_20150924_1833'),
    ]

    operations = [
        migrations.AlterField(
            model_name='all_course',
            name='department_name',
            field=models.CharField(max_length=50),
        ),
    ]
