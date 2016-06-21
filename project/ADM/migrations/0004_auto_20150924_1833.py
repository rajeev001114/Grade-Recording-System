# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ADM', '0003_all_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='all_course',
            name='department_name',
            field=models.ForeignKey(to='ADM.All_deprtment'),
        ),
    ]
