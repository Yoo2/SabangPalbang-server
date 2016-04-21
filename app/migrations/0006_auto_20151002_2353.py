# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_remove_room_location'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='roomimage',
            name='image_path',
        ),
        migrations.AddField(
            model_name='roomimage',
            name='image',
            field=models.ImageField(height_field=b'image_height', width_field=b'image_width', upload_to=b'media/room_img', blank=True, help_text=b'Room Picture', null=True, verbose_name=b'Room Picture'),
        ),
        migrations.AddField(
            model_name='roomimage',
            name='image_height',
            field=models.PositiveIntegerField(default=b'100', null=True, editable=False, blank=True),
        ),
        migrations.AddField(
            model_name='roomimage',
            name='image_width',
            field=models.PositiveIntegerField(default=b'100', null=True, editable=False, blank=True),
        ),
        migrations.AlterField(
            model_name='roomimage',
            name='room',
            field=models.ForeignKey(related_name='images', to='app.Room'),
        ),
    ]
