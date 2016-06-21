# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ADM', '0010_auto_20150926_1332'),
        ('TCH', '0004_courseallotment_is_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personinformation',
            name='streamid',
        ),
        migrations.AddField(
            model_name='personinformation',
            name='departmentid',
            field=models.ForeignKey(default='', to='ADM.All_deprtment'),
            preserve_default=False,
        ),
    ]
