from django.views.generic import ListView
from post.models import Post
from django.conf import settings
from django.contrib.flatpages.models import FlatPage
from django.shortcuts import get_object_or_404

class PostListView(ListView):

	template_name = 'flatpages/home.html' 

	def get_queryset(self):
		url = self.request.path_info
		if not url.startswith('/'):
			url = '/' + url
		# get flatpage from request
		self.flatpage = get_object_or_404(FlatPage, url__exact=url, sites__exact=settings.SITE_ID)
		return Post.objects.all()
	
	def get_context_data(self, **kwargs):
		context = super(PostListView, self).get_context_data(**kwargs)
		# add flatpage to context
		context['flatpage'] = self.flatpage
		return context
		

			

	
