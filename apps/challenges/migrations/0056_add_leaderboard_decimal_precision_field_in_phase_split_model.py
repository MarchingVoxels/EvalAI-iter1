# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-07-19 18:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challenges', '0055_add_is_leaderboard_order_descending_in_phase_split_model'),
    ]

    operations = [
        migrations.AddField(
            model_name='challengephasesplit',
            name='leaderboard_decimal_precision',
            field=models.PositiveIntegerField(default=2),
        ),
    ]
