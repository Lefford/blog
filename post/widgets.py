from django.forms import widgets
from django.utils.safestring import mark_safe

class CKEditorWidget(widgets.Textarea):
	"""
	CKEDITOR widget
	"""
	
	def __init__(self, attrs=None):
		if not attrs:
			attrs =  {'class': 'ckeditor'}

		super(CKEditorWidget, self).__init__(attrs)

	class Media:
		js = ('ckeditor/ckeditor.js',)

	def render(self, name, value , attrs=None):
		std_markup = super(CKEditorWidget, self).render(name, value, attrs)
		js_markup = std_markup +   u"""<script type=text/javascript>
					           $ = django.jQuery;
						   $('#%s').ckeditor();
				                 </script>
			                     """ % (attrs['id'])

		return mark_safe(js_markup)
