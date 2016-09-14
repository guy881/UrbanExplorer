# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-09-08 07:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=240)),
            ],
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('register_image', models.ImageField(blank=True, null=True, upload_to='register_images', verbose_name='register image')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(db_index=True, max_length=240)),
                ('answer', models.CharField(max_length=240)),
            ],
        ),
        migrations.CreateModel(
            name='Riddle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='nazwa')),
                ('description', models.TextField(verbose_name='opis')),
                ('long', models.DecimalField(decimal_places=6, max_digits=9)),
                ('lat', models.DecimalField(decimal_places=6, max_digits=9)),
                ('times_resolved', models.DecimalField(decimal_places=0, max_digits=9)),
                ('rate', models.DecimalField(decimal_places=3, max_digits=5)),
                ('logo_image', models.ImageField(blank=True, null=True, upload_to='logos', verbose_name='logo image')),
                ('min_image', models.ImageField(blank=True, null=True, upload_to='min_logos', verbose_name='min image')),
            ],
        ),
        migrations.AddField(
            model_name='question',
            name='riddle',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='riddles.Riddle'),
        ),
        migrations.AddField(
            model_name='images',
            name='riddle',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='riddles.Riddle'),
        ),
        migrations.AddField(
            model_name='category',
            name='riddles',
            field=models.ManyToManyField(to='riddles.Riddle'),
        ),
    ]