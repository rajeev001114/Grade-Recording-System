# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import MSG.models


class Migration(migrations.Migration):

    dependencies = [
        ('MSG', '0016_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='content',
            name='file',
        ),
        migrations.AddField(
            model_name='content',
            name='filename',
            field=models.FileField(null=True, upload_to=MSG.models.get_upload_file_name),
        ),
    ]
