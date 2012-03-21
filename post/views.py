from django.views.generic import TemplateView, DetailView, View
from django.views.generic.list import BaseListView
from django.views.generic.detail import BaseDetailView
from django.http import HttpResponseRedirect
from django.conf import settings
from django.shortcuts import get_object_or_404
from post.models import ParentPage, ContentBlock, Post
import os

class PageView(TemplateView):

	template_name = 'flatpages/default.html'
		
	def get(self, request, *args, **kwargs):
		url = request.path_info
		print url
		if not url.endswith('/') and settings.APPEND_SLASH:
			return HttpResponseRedirect(url + '/')
		if not url.startswith('/'):
			url = url + '/'
			kwargs.update({'url': url})
		context = self.get_context_data(**kwargs)
		# rather had return an templateresponse at thia moment i dont know how to get it right in process_template_response
		return self.render_to_response(context).render()
	
	def get_context_data(self, **kwargs):
		context = super(PageView, self).get_context_data(**kwargs)
		url = kwargs['url']
		page = get_object_or_404(ParentPage, url__exact=url, sites__id__exact=settings.SITE_ID)
		context.update({'page': page})
		return context

class PageMixin(object):
	def get_context_data(self, **kwargs):
		url = self.request.path_info
		context = super(PageMixin, self).get_context_data(**kwargs)
		try:
			page = ParentPage.objects.get(url=url, sites__id__exact=settings.SITE_ID)
			context.update({'page': page})
		except ParentPage.DoesNotExist:
			# callback to get the page for a detail page
			url = os.path.dirname(url)
			url = url + '/'
			page = ParentPage.objects.get(alias_url=url, sites__id__exact=settings.SITE_ID)
			context.update({'page': page})
		return context

class ContentBlockMixin(object):
	def get_context_data(self, **kwargs):
		context = super(ContentBlockMixin, self).get_context_data(**kwargs)
		contentblocks = ContentBlock.objects.all()
		context.update({'contentblocks': contentblocks})
		return context

class PostMixin(object):
	def get_context_data(self, **kwargs):
		context = super(PostMixin, self).get_context_data(**kwargs)
		posts = Post.objects.all()
		context.update({'post': posts})
		return context

class CMSPage(ContentBlockMixin, PageMixin):
	"""
	This view construct a page with contentblock and page

	This code is still experimental, first timer classed based view 
	"""

class PostListView(CMSPage, BaseListView, PageView):
	template_name = 'flatpages/blog.html'
	context_object_name = 'posts'
	model = Post

class PostDetailView(CMSPage, DetailView):	
	template_name = 'flatpages/post-detail.html'
	context_object_name = 'post'
	model = Post

class TwitterView(View):
	pass

class JSONResponseMixin(object):
	pass

class TwitterMixin(object):
	pass

