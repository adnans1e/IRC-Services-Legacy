# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2018-03-07 22:15
from __future__ import unicode_literals

from django.db import migrations, models
import services.models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0054_auto_20180228_1423'),
    ]

    operations = [
        migrations.AddField(
            model_name='nationality',
            name='name_ti',
            field=models.CharField(blank=True, default='', max_length=256, verbose_name='name in Tigrinya'),
        ),
        migrations.AddField(
            model_name='provider',
            name='address_ti',
            field=models.TextField(blank=True, default='', verbose_name='provider address in Tigrinya'),
        ),
        migrations.AddField(
            model_name='provider',
            name='description_ti',
            field=models.TextField(blank=True, default='', verbose_name='description in Tigrinya'),
        ),
        migrations.AddField(
            model_name='provider',
            name='focal_point_name_ti',
            field=models.CharField(blank=True, default='', max_length=256, validators=[services.models.blank_or_at_least_one_letter], verbose_name='focal point name in Tigrinya'),
        ),
        migrations.AddField(
            model_name='provider',
            name='name_ti',
            field=models.CharField(blank=True, default='', max_length=256, validators=[services.models.blank_or_at_least_one_letter], verbose_name='Name in Tigrinya'),
        ),
        migrations.AddField(
            model_name='providertype',
            name='name_ti',
            field=models.CharField(blank=True, default='', max_length=256, verbose_name='Name in Tigrinya'),
        ),
        migrations.AddField(
            model_name='selectioncriterion',
            name='text_ti',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AddField(
            model_name='service',
            name='additional_info_ti',
            field=models.TextField(blank=True, default='', verbose_name='Additional information in Tigrinya'),
        ),
        migrations.AddField(
            model_name='service',
            name='address_city_ti',
            field=models.TextField(blank=True, default='', null=True, verbose_name='Address (city) in Tigrinya'),
        ),
        migrations.AddField(
            model_name='service',
            name='address_floor_ti',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='service',
            name='address_ti',
            field=models.TextField(blank=True, default='', null=True, verbose_name='Address (street) in Tigrinya'),
        ),
        migrations.AddField(
            model_name='service',
            name='description_ti',
            field=models.TextField(blank=True, default='', verbose_name='Description in Tigrinya'),
        ),
        migrations.AddField(
            model_name='service',
            name='languages_spoken_ti',
            field=models.TextField(blank=True, default='', verbose_name='Languages spoken in Tigrinya'),
        ),
        migrations.AddField(
            model_name='service',
            name='name_ti',
            field=models.CharField(blank=True, default='', max_length=256, verbose_name='Name in Tigrinya'),
        ),
        migrations.AddField(
            model_name='servicearea',
            name='name_ti',
            field=models.CharField(blank=True, default='', max_length=256, verbose_name='Name in Tigrinya'),
        ),
        migrations.AddField(
            model_name='servicetype',
            name='comments_ti',
            field=models.CharField(blank=True, default='', max_length=512, verbose_name='comments in Tigrinya'),
        ),
        migrations.AddField(
            model_name='servicetype',
            name='name_ti',
            field=models.CharField(blank=True, default='', max_length=256, verbose_name='name in Tigrinya'),
        ),
        migrations.AlterField(
            model_name='service',
            name='status',
            field=models.CharField(choices=[('draft', 'draft'), ('current', 'current'), ('rejected', 'rejected'), ('canceled', 'canceled'), ('archived', 'archived'), ('private', 'private')], default='draft', max_length=10, verbose_name='status'),
        ),
    ]
