from django.conf.urls.defaults import patterns, include, url
from post.views import PageView, PostListView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from post.models import Post 

urlpatterns = patterns('',
	url(r'^$', PostListView.as_view(model=Post, template_name='flatpages/home.html'), name='home'),
	url(r'^page/$', PostListView.as_view(model=Post, template_name='flatpages/post-list.html'), name='page-post'),
	url(r'^page/detail/(?P<pk>[\d]+)/$', DetailView.as_view(model=Post, template_name='flatpages/post-detail.html'), name='post-detail'),
)
