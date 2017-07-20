from __future__ import unicode_literals
from django.db import models
import os
from datetime import datetime,date
from django import forms
from django.contrib.auth.models import User
import uuid

from django.db import models
from django import forms
#from django.contrib.admin.widgets import AdminDateWidget

class UserID(models.Model):
	email = models.CharField(max_length=64)
	username = models.OneToOneField(User)
	username1 = models.CharField(max_length=64)
	password = models.CharField(max_length=64)
	art_count = models.IntegerField(default=1, null = True)
	kw_count = models.IntegerField(default=0, null = True)
	def __str__(self):
		return self.username1

	
class Keyword(models.Model):
	point = models.CharField(max_length=256)
	word = models.CharField(max_length=256)
	gif1 = models.CharField(max_length=128)
	gif2 = models.CharField(max_length=128)
	gif3 = models.CharField(max_length=128)
	gif4 = models.CharField(max_length=128)
	gif5 = models.CharField(max_length=128)
	gif6 = models.CharField(max_length=128)
	gif7 = models.CharField(max_length=128)
	gif8 = models.CharField(max_length=128)
	gif9 = models.CharField(max_length=128)
	gif10 = models.CharField(max_length=128)
	count1 = models.IntegerField(default=0, null = True)
	count2 = models.IntegerField(default=0, null = True)
	count3 = models.IntegerField(default=0, null = True)
	count4 = models.IntegerField(default=0, null = True)
	count5 = models.IntegerField(default=0, null = True)
	count6 = models.IntegerField(default=0, null = True)
	count7 = models.IntegerField(default=0, null = True)
	count8 = models.IntegerField(default=0, null = True)
	count9 = models.IntegerField(default=0, null = True)
	count10 = models.IntegerField(default=0, null = True)
	def __str__(self):
		return self.word
	
class UserLikedGif(models.Model):
	user_id = models.ForeignKey(UserID,verbose_name = "User")
	gif_id = models.ForeignKey(Keyword,verbose_name="KeyWord Gifs")
	liked = models.CharField(max_length=16)
	def __str__(self):
		return self.user_id.username1 + "-" + self.gif_id.word

class Article(models.Model):
	link = models.CharField(max_length=512)
	title = models.CharField(max_length=256)
	kw1 = models.ForeignKey(Keyword,verbose_name="KeyWord Gifs1",related_name="article_kw1")
	kw2 =	models.ForeignKey(Keyword,verbose_name="KeyWord Gifs2",related_name="article_kw2")
	kw3 = models.ForeignKey(Keyword,verbose_name="KeyWord Gifs3",related_name="article_kw3")
	kw4 = models.ForeignKey(Keyword,verbose_name="KeyWord Gifs4",related_name="article_kw4")
	kw5 = models.ForeignKey(Keyword,verbose_name="KeyWord Gifs5",related_name="article_kw5")
	def __str__(self):
		return self.title
		
class ArticleCount(models.Model):
	count = models.IntegerField(default=0, null = True)
	name = models.CharField(max_length=2)

