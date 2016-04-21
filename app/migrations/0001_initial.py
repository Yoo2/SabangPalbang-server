# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('location', models.IntegerField()),
                ('floor', models.IntegerField()),
                ('security_deposit', models.IntegerField()),
                ('month_price', models.IntegerField()),
                ('management_cost', models.IntegerField(null=True)),
                ('pet', models.BooleanField()),
                ('term', models.CharField(max_length=200)),
                ('etc', models.TextField(null=True)),
                ('detail', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='RoomImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image_path', models.CharField(max_length=200)),
                ('room', models.ForeignKey(to='app.Room')),
            ],
        ),
    ]
