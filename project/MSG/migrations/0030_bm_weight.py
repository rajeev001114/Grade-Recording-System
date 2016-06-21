# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ADM', '0010_auto_20150926_1332'),
        ('TCH', '0004_courseallotment_is_active'),
        ('MSG', '0029_auto_20150929_0833'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bm_weight',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('bmoocs_weight', models.IntegerField()),
                ('personid', models.ForeignKey(to='TCH.Personinformation')),
                ('sessionid', models.ForeignKey(to='ADM.Academic_session')),
            ],
        ),
    ]
