# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ADM', '0008_academic_session'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='academic_session',
            options={'get_latest_by': 'year'},
        ),
    ]
