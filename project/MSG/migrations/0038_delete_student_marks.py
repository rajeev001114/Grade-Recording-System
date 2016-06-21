# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MSG', '0037_auto_20151007_1842'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Student_marks',
        ),
    ]
