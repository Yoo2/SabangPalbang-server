# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_room_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='kitchen',
            field=models.BooleanField(choices=[(True, b'yes'), (False, b'no')]),
        ),
        migrations.AlterField(
            model_name='room',
            name='microwave',
            field=models.BooleanField(choices=[(True, b'yes'), (False, b'no')]),
        ),
        migrations.AlterField(
            model_name='room',
            name='pet',
            field=models.BooleanField(choices=[(True, b'yes'), (False, b'no')]),
        ),
        migrations.AlterField(
            model_name='room',
            name='tv',
            field=models.BooleanField(choices=[(True, b'yes'), (False, b'no')]),
        ),
        migrations.AlterField(
            model_name='room',
            name='two_room',
            field=models.BooleanField(choices=[(True, b'yes'), (False, b'no')]),
        ),
        migrations.AlterField(
            model_name='room',
            name='veranda',
            field=models.BooleanField(choices=[(True, b'yes'), (False, b'no')]),
        ),
    ]
