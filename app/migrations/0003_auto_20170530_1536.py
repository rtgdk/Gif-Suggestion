# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_userid_username1'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleCount',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('count', models.IntegerField(default=1, null=True)),
                ('name', models.CharField(max_length=2)),
            ],
        ),
        migrations.AddField(
            model_name='userid',
            name='art_count',
            field=models.IntegerField(default=1, null=True),
        ),
        migrations.AddField(
            model_name='userid',
            name='kw_count',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
