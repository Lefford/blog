from django.views.generic import TemplateView, ListView
from django.http import HttpResponseRedirect
from django.conf import settings
from django.shortcuts import get_object_or_404
from post.models import ParentPage, ContentBlock

class PageView(TemplateView):

	template_name = 'flatpages/base.html'
		
	def get(self, request, *args, **kwargs):
		url = kwargs['url']
		print url
		if not url.endswith('/') and settings.APPEND_SLASH:
			return HttpResponseRedirect(url + '/')
		if not url.startswith('/'):
			url = url + '/'
			kwargs.update({'url': url})
		context = self.get_context_data(**kwargs)
		return self.render_to_response(context).render()

	def get_context_data(self, **kwargs):
		url = kwargs.pop('url')
		context = super(PageView, self).get_context_data(**kwargs)
		page = get_object_or_404(ParentPage, url__exact=url, sites__id__exact=settings.SITE_ID)
		context.update({'page': page})
		return context

class PostListView(ListView):
	
	def get_context_data(self, **kwargs):
		context = super(PostListView, self).get_context_data(**kwargs)
		page_context = PageView().get_context_data(url=self.request.path_info)
		context.update(page_context)
		contentblocks = ContentBlock.objects.all().order_by('show_after')
		context.update({'contentblocks': contentblocks})
		return context
