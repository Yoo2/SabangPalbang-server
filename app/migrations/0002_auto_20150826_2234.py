# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='kitchen',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='room',
            name='veranda',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='room',
            name='pet',
            field=models.BooleanField(default=False),
        ),
    ]
