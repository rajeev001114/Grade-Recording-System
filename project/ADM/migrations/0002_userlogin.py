# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ADM', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Userlogin',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('usertypeid', models.IntegerField(default=1)),
                ('status', models.BooleanField(default=0)),
                ('last_login', models.DateTimeField(default=django.utils.timezone.now)),
                ('nooflogins', models.IntegerField(default=0, null=True)),
                ('user', models.OneToOneField(related_name='login', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
