from django.contrib.flatpages.models import FlatPage
from django.template import Library, Node

register = Library()

def header_menu():
	header_pages = FlatPage.objects.all()

	menu = "<ul class='menu-buttons'>"
	for page in header_pages:
		li = "<li class='menu-item'><a href='{0}'>{1}</a>".format(page.url, page.title)
		menu+=li
	menu+="</ul>"

	return menu

register.simple_tag(header_menu)
