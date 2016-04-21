# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0021_mydevice'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mydevice',
            name='user',
        ),
        migrations.DeleteModel(
            name='MyDevice',
        ),
    ]
