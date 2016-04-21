# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20151008_2253'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='roomimage',
            unique_together=set([('image',)]),
        ),
    ]
