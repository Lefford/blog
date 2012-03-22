from django.conf.urls.defaults import patterns, include, url
from post.views import PageView, PostListView
from django.views.generic.detail import DetailView

urlpatterns = patterns('',
	url(r'^$', PostListView.as_view(), name='home'),
	url(r'^page/$', ListView.as_view(model=Post, template_name='post/post-list.html'), name='page-post'),
	url(r'^page/detail/(?P<pk>[\d]+)/$', DetailView.as_view(model=Post, template_name='flatpages/post-detail.html'), name='post-detail'),
)
