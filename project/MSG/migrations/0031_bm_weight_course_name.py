# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MSG', '0030_bm_weight'),
    ]

    operations = [
        migrations.AddField(
            model_name='bm_weight',
            name='course_name',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
