# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20150826_2234'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='microwave',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='room',
            name='tv',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='room',
            name='two_room',
            field=models.BooleanField(default=False),
        ),
    ]
