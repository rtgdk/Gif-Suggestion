# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('link', models.CharField(max_length=512)),
                ('title', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Keyword',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('word', models.CharField(max_length=256)),
                ('gif1', models.CharField(max_length=128)),
                ('gif2', models.CharField(max_length=128)),
                ('gif3', models.CharField(max_length=128)),
                ('gif4', models.CharField(max_length=128)),
                ('gif5', models.CharField(max_length=128)),
                ('gif6', models.CharField(max_length=128)),
                ('gif7', models.CharField(max_length=128)),
                ('gif8', models.CharField(max_length=128)),
                ('gif9', models.CharField(max_length=128)),
                ('gif10', models.CharField(max_length=128)),
                ('count1', models.IntegerField(default=0, null=True)),
                ('count2', models.IntegerField(default=0, null=True)),
                ('count3', models.IntegerField(default=0, null=True)),
                ('count4', models.IntegerField(default=0, null=True)),
                ('count5', models.IntegerField(default=0, null=True)),
                ('count6', models.IntegerField(default=0, null=True)),
                ('count7', models.IntegerField(default=0, null=True)),
                ('count8', models.IntegerField(default=0, null=True)),
                ('count9', models.IntegerField(default=0, null=True)),
                ('count10', models.IntegerField(default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserID',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.CharField(max_length=64)),
                ('password', models.CharField(max_length=64)),
                ('username', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserLikedGif',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('liked', models.CharField(max_length=32)),
                ('gif_id', models.ForeignKey(verbose_name='KeyWord Gifs', to='app.Keyword')),
                ('user_id', models.ForeignKey(verbose_name='User', to='app.UserID')),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='kw1',
            field=models.ForeignKey(related_name='article_kw1', verbose_name='KeyWord Gifs1', to='app.Keyword'),
        ),
        migrations.AddField(
            model_name='article',
            name='kw2',
            field=models.ForeignKey(related_name='article_kw2', verbose_name='KeyWord Gifs2', to='app.Keyword'),
        ),
        migrations.AddField(
            model_name='article',
            name='kw3',
            field=models.ForeignKey(related_name='article_kw3', verbose_name='KeyWord Gifs3', to='app.Keyword'),
        ),
        migrations.AddField(
            model_name='article',
            name='kw4',
            field=models.ForeignKey(related_name='article_kw4', verbose_name='KeyWord Gifs4', to='app.Keyword'),
        ),
        migrations.AddField(
            model_name='article',
            name='kw5',
            field=models.ForeignKey(related_name='article_kw5', verbose_name='KeyWord Gifs5', to='app.Keyword'),
        ),
    ]
