# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20151003_2224'),
    ]

    operations = [
        migrations.RenameField(
            model_name='roomimage',
            old_name='room',
            new_name='room_id',
        ),
    ]
