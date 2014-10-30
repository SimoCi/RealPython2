from django.conf.urls import patterns, url
from blog import views

urlpatterns = patterns(
	'blog.views',
	url(r'^$', views.index, name='index'),
	# this use slugs
	# url(r'^(?P<slug>\d+)/$', views.post, name='post'),
	url(r'^(?P<slug>\w+)/$', views.post, name='post'),
	# url(r'^(?P<slug>\w\d+)/$', views.post, name='post'),
	)