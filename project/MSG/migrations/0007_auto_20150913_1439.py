# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MSG', '0006_auto_20150913_1338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grade_policy',
            name='gp_id',
            field=models.IntegerField(),
        ),
    ]
