# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-10-19 10:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('avi', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tutorialmodel',
            name='fib_num',
        ),
    ]
