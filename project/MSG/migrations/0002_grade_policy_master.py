# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MSG', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Grade_policy',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('gp_id', models.IntegerField(max_length=20)),
                ('abbreviation', models.CharField(max_length=4)),
                ('evaluation_id', models.CharField(max_length=20)),
                ('total', models.IntegerField(max_length=3)),
                ('mandatory', models.IntegerField(max_length=3)),
                ('weight', models.IntegerField(max_length=3)),
                ('consolidated', models.CharField(max_length=1)),
                ('seq_number', models.IntegerField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Master',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('teacher_id', models.IntegerField(max_length=20)),
                ('gp_id', models.IntegerField(max_length=20)),
            ],
        ),
    ]
