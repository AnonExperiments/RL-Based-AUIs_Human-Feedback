# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2024-09-11 15:45
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('human_feedback_api', '0002_auto_20170907_1124'),
    ]

    operations = [
        migrations.AddField(
            model_name='clip',
            name='domain',
            field=models.CharField(blank=True, db_index=True, max_length=255, null=None),
        ),
        migrations.AddField(
            model_name='comparison',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='compares', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='sorttree',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='sort_trees', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
