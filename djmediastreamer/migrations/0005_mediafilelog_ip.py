# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-27 16:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djmediastreamer', '0004_usersettings'),
    ]

    operations = [
        migrations.AddField(
            model_name='mediafilelog',
            name='ip',
            field=models.GenericIPAddressField(default='127.0.0.1'),
        ),
    ]