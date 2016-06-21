# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TCH', '0006_auto_20160422_0907'),
    ]

    operations = [
        migrations.RenameField(
            model_name='evaluation_table',
            old_name='eval_n0',
            new_name='eval_no',
        ),
    ]
