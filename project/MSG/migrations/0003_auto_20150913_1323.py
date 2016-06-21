# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MSG', '0002_grade_policy_master'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseGrade',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('teacher_id', models.IntegerField()),
                ('gp_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ErrorContent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('systype', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=100)),
                ('errorcode', models.CharField(default=b'null', unique=True, max_length=20)),
                ('error_message', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Master',
        ),
        migrations.DeleteModel(
            name='Publisher',
        ),
        migrations.AlterField(
            model_name='grade_policy',
            name='gp_id',
            field=models.ForeignKey(to='MSG.CourseGrade'),
        ),
        migrations.AlterField(
            model_name='grade_policy',
            name='mandatory',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='grade_policy',
            name='seq_number',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='grade_policy',
            name='total',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='grade_policy',
            name='weight',
            field=models.IntegerField(),
        ),
    ]
