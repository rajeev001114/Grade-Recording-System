# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MSG', '0025_auto_20150919_0749'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student_marks',
            name='total',
            field=models.FloatField(),
        ),
    ]
