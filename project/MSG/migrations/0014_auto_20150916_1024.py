# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MSG', '0013_uploadfile'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UploadFile',
            new_name='uploadedfiles',
        ),
    ]
