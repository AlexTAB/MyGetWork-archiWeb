# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(verbose_name='Name', max_length=30)),
                ('mail', models.CharField(verbose_name='Email', max_length=80)),
                ('username', models.CharField(verbose_name='Username', max_length=20)),
                ('password', models.CharField(verbose_name='Password', max_length=20)),
            ],
        ),
    ]
