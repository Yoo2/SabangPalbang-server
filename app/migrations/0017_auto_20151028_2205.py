# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_auto_20151027_2219'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='pet',
        ),
        migrations.AddField(
            model_name='room',
            name='air_conditioner',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='room',
            name='bed',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='room',
            name='desk',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='room',
            name='fire_type',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='room',
            name='washer',
            field=models.IntegerField(null=True),
        ),
    ]
