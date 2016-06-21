# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MSG', '0024_bm_weight'),
    ]

    operations = [
        migrations.CreateModel(
            name='Policy_weight',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('teacher_id', models.IntegerField()),
                ('course_id', models.CharField(max_length=45)),
                ('pweight', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='student_marks',
            name='total',
            field=models.IntegerField(default=23),
            preserve_default=False,
        ),
    ]
