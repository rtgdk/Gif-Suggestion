# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userid',
            name='username1',
            field=models.CharField(default='old', max_length=64),
            preserve_default=False,
        ),
    ]
