# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_auto_20151028_2246'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.CharField(max_length=200)),
                ('date', models.CharField(max_length=200)),
                ('board', models.ForeignKey(related_name='comments', to='app.Board')),
                ('user', models.ForeignKey(related_name='comments', to='app.User')),
            ],
        ),
        migrations.RemoveField(
            model_name='boardcomment',
            name='board',
        ),
        migrations.RemoveField(
            model_name='boardcomment',
            name='user',
        ),
        migrations.DeleteModel(
            name='BoardComment',
        ),
    ]
