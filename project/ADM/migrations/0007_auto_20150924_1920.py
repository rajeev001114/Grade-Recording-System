# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ADM', '0006_auto_20150924_1847'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='all_course',
            name='department_name',
        ),
        migrations.AddField(
            model_name='all_course',
            name='dpname',
            field=models.ForeignKey(to_field=b'department_name', blank=True, to='ADM.All_deprtment', null=True),
        ),
        migrations.AlterField(
            model_name='all_deprtment',
            name='department_name',
            field=models.CharField(unique=True, max_length=50),
        ),
    ]
