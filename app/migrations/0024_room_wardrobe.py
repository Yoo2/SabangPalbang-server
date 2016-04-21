# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0023_room_elevator'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='wardrobe',
            field=models.IntegerField(default=0),
        ),
    ]
