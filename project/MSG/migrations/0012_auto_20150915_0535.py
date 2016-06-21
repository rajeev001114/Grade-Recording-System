# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MSG', '0011_auto_20150915_0534'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grade_policy',
            name='gp_id',
            field=models.CharField(max_length=50),
        ),
    ]
