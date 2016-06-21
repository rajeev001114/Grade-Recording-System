# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MSG', '0010_auto_20150915_0510'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursegrade',
            name='course_id',
            field=models.CharField(max_length=45),
        ),
        migrations.AlterField(
            model_name='coursegrade',
            name='gp_id',
            field=models.CharField(max_length=50),
        ),
    ]
