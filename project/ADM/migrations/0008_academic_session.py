# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ADM', '0007_auto_20150924_1920'),
    ]

    operations = [
        migrations.CreateModel(
            name='Academic_session',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('year', models.CharField(max_length=20)),
                ('semester', models.IntegerField()),
                ('is_active', models.BooleanField(default=1)),
            ],
        ),
    ]
