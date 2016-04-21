# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20150827_0006'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='area',
            field=models.IntegerField(default=0),
        ),
    ]
