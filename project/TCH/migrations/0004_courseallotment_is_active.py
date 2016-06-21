# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TCH', '0003_auto_20150926_1520'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseallotment',
            name='is_active',
            field=models.BooleanField(default=1),
        ),
    ]
