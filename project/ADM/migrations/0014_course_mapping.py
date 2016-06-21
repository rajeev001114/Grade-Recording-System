# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ADM', '0013_moodle'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course_mapping',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mdl_cid', models.CharField(max_length=20)),
                ('is_active', models.BooleanField(default=1)),
                ('cid', models.ForeignKey(blank=True, to='ADM.All_course', null=True)),
            ],
        ),
    ]
