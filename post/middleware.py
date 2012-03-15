from post.models import ParentPage
from django.http import Http404
from django.conf import settings
from post.views import PageView
from django.template.response import TemplateResponse

class PageFallbackMiddleware(object):
	def process_response(self, request, response):
		print 'Triggered'
		if response.status_code != 404:
			return response
		try:
			return PageView.as_view()(request, url=request.path_info)
		except Http404:
			return response
		except:
			if settings.DEBUG:
				raise
			return response
