# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_auto_20151011_1946'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='size',
            field=models.IntegerField(default=0),
        ),
    ]
