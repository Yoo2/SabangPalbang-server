# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import app.models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20151002_2353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roomimage',
            name='image',
            field=models.ImageField(height_field=b'image_height', width_field=b'image_width', upload_to=app.models.PathAndRename(b'media/room_img'), blank=True, help_text=b'Room Picture', null=True, verbose_name=b'Room Picture'),
        ),
    ]
