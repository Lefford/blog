from post.models import ParentPage
from django.template import Library, Node

register = Library()

def header_menu():
	"""
	Render menu horizontal
	"""
	header_pages = ParentPage.objects.all().order_by('show_after')

	menu = "<ul class='menu-buttons'>"
	for index, page in enumerate(header_pages):
		li = "<li class='menu item_{0}'><a href='{1}'>{2}</a>".format(index, page.url, page.title)
		menu+=li
	menu+="</ul>"

	return menu

register.simple_tag(header_menu)
