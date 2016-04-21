# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0022_auto_20151102_2359'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='elevator',
            field=models.IntegerField(default=0),
        ),
    ]
