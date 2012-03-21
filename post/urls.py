from django.conf.urls.defaults import patterns, include, url
from post.views import PostListView, PostDetailView 
from post.models import Post 

urlpatterns = patterns('',
	url(r'^$', PostListView.as_view(), name='home'),
	url(r'^blog/$', PostListView.as_view(), name='blog'),
	url(r'^blog/entry/(?P<pk>[\d]+)$', PostDetailView.as_view(), name='post-detail'),
)
