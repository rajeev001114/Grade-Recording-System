# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MSG', '0033_bm_policy_weight'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student_marks',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('roll_no', models.CharField(default=b'0', max_length=30)),
                ('total', models.FloatField()),
            ],
        ),
    ]
