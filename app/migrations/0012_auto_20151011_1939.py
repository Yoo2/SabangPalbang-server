# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_auto_20151011_1931'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='etc',
        ),
        migrations.AddField(
            model_name='room',
            name='hash1',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='room',
            name='hash2',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='room',
            name='hash3',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
