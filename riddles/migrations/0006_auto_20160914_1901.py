# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-09-14 17:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('riddles', '0005_riddle_rate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='riddle',
            name='description',
            field=models.TextField(verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='riddle',
            name='name',
            field=models.CharField(max_length=50, verbose_name='name'),
        ),
    ]
