# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20170530_1536'),
    ]

    operations = [
        migrations.AddField(
            model_name='keyword',
            name='point',
            field=models.CharField(default='Old', max_length=256),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='articlecount',
            name='count',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='userlikedgif',
            name='liked',
            field=models.CharField(max_length=16),
        ),
    ]
