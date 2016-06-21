# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MSG', '0005_coursegrade_errorcontent_grade_policy'),
    ]

    operations = [
        migrations.RenameField(
            model_name='grade_policy',
            old_name='evaluation_id',
            new_name='assignment',
        ),
    ]
