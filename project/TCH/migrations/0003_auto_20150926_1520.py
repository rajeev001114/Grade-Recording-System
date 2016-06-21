# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ADM', '0010_auto_20150926_1332'),
        ('TCH', '0002_auto_20150926_1225'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='courseallotment',
            name='enddate',
        ),
        migrations.RemoveField(
            model_name='courseallotment',
            name='roleid',
        ),
        migrations.RemoveField(
            model_name='courseallotment',
            name='startdate',
        ),
        migrations.AddField(
            model_name='courseallotment',
            name='sessionid',
            field=models.ForeignKey(default=10, to='ADM.Academic_session'),
            preserve_default=False,
        ),
    ]
