# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TCH', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='personinformation',
            old_name='isactive',
            new_name='is_active',
        ),
    ]
