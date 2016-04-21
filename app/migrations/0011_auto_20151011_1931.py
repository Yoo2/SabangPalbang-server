# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import app.models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20151009_2006'),
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('content', models.CharField(max_length=200)),
                ('cost', models.CharField(max_length=200)),
                ('item', models.CharField(max_length=200)),
                ('date', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='BoardComment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.CharField(max_length=200)),
                ('date', models.CharField(max_length=200)),
                ('board', models.ForeignKey(related_name='comments', to='app.Board')),
            ],
        ),
        migrations.CreateModel(
            name='BoardImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(height_field=b'image_height', width_field=b'image_width', upload_to=app.models.PathAndRename(b'board_img'), blank=True, help_text=b'Board Picture', null=True, verbose_name=b'Board Picture')),
                ('image_height', models.PositiveIntegerField(default=b'100', null=True, editable=False, blank=True)),
                ('image_width', models.PositiveIntegerField(default=b'100', null=True, editable=False, blank=True)),
                ('board', models.ForeignKey(related_name='images', to='app.Board')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_id', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='boardcomment',
            name='user',
            field=models.ForeignKey(related_name='comments', to='app.User'),
        ),
        migrations.AddField(
            model_name='board',
            name='user',
            field=models.ForeignKey(related_name='boards', to='app.User'),
        ),
        migrations.AlterUniqueTogether(
            name='boardimage',
            unique_together=set([('image',)]),
        ),
    ]
