# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_auto_20151015_1236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='kitchen',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='room',
            name='microwave',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='room',
            name='pet',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='room',
            name='tv',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='room',
            name='two_room',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='room',
            name='veranda',
            field=models.IntegerField(),
        ),
    ]
