from django.contrib import admin
from app.models import UserID,Keyword,UserLikedGif,Article,ArticleCount
admin.site.register(UserID)
admin.site.register(Keyword)
admin.site.register(UserLikedGif)
admin.site.register(Article)
admin.site.register(ArticleCount)
# Register your models here.
