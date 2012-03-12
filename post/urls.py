from django.conf.urls.defaults import patterns, include, url
from django.views.generic.list import ListView 
from django.views.generic.detail import DetailView
from post.views import PostListView
from post.models import Post

urlpatterns = patterns('',
	url(r'^$', PostListView.as_view(), name='home'),
	url(r'^page/$', ListView.as_view(model=Post, template_name='post/post-list.html'), name='page-post'),
	url(r'^page/detail/(?P<pk>[\d]+)/$', DetailView.as_view(model=Post, template_name='flatpages/post-detail.html'), name='post-detail'),
)
