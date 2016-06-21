# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MSG', '0022_bm_weight'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Bm_weight',
        ),
    ]
