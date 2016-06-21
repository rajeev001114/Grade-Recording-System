# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ADM', '0011_teacher_mapping'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student_mapping',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mdl_id', models.CharField(max_length=20)),
                ('mooc_id', models.CharField(max_length=20)),
                ('is_active', models.BooleanField(default=1)),
            ],
        ),
    ]
