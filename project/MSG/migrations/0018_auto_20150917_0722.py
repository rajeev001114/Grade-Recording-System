# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MSG', '0017_auto_20150917_0707'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='content',
            name='filename',
        ),
        migrations.AddField(
            model_name='content',
            name='file',
            field=models.FileField(default=12, upload_to=b'.'),
            preserve_default=False,
        ),
    ]
