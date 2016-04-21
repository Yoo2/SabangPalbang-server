# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0019_auto_20151030_2118'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='device_token',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='room',
            name='area',
            field=models.IntegerField(default=1),
        ),
    ]
