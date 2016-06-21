# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MSG', '0014_auto_20150916_1024'),
    ]

    operations = [
        migrations.DeleteModel(
            name='uploadedfiles',
        ),
    ]
