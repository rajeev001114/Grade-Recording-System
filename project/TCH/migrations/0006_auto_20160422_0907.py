# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TCH', '0005_auto_20150929_1338'),
    ]

    operations = [
        migrations.CreateModel(
            name='Evaluation_marks',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('roll_no', models.CharField(max_length=50)),
                ('marks', models.FloatField()),
                ('is_active', models.BooleanField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Evaluation_table',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('eval_name', models.CharField(max_length=30)),
                ('eval_n0', models.CharField(max_length=30)),
                ('max_marks', models.FloatField()),
                ('is_active', models.BooleanField(default=1)),
                ('courseallotid', models.ForeignKey(to='TCH.Courseallotment')),
            ],
        ),
        migrations.AddField(
            model_name='evaluation_marks',
            name='evalid',
            field=models.ForeignKey(to='TCH.Evaluation_table'),
        ),
    ]
