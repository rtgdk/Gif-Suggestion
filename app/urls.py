from django.conf.urls import url
from app import views
urlpatterns = [
url(r'^$', views.index, name='index'),
url(r'^article/$', views.article, name='article'),
url(r'^login/$', views.login, name='login'),
url(r'^logout/$', views.logout, name='logout'),
url(r'^addarticle/$', views.addarticle, name='add article'),
url(r'^register/$', views.register, name='register'),
#url(r'^search/(?P<key>[-\w]+)$', views.ajaxsearch, name='search'),
]
