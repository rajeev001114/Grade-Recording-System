# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ADM', '0002_userlogin'),
    ]

    operations = [
        migrations.CreateModel(
            name='All_course',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('course_code', models.CharField(max_length=10)),
                ('course_name', models.CharField(max_length=50)),
                ('department_name', models.CharField(max_length=50)),
                ('is_active', models.BooleanField(default=1)),
            ],
        ),
    ]
