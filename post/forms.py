from django import forms
from post.models import ParentPage, ChildPage, ContentBlock
from post.widgets import CKEditorWidget

class ParentPageForm(forms.ModelForm):
	"""
	Modelform for parent page
	"""

	def __init__(self, *args, **kwargs):
		super(ParentPageForm, self).__init__(*args, **kwargs)
		instance = self.instance
		if instance:
			# exlude option order page after it's self
			self.fields['show_after'].queryset=ParentPage.objects.exclude(id=instance.id)

	class Meta:
		model = ParentPage

class ChildPageForm(forms.ModelForm):

	"""
	modelform child page
	"""
	
	def __init__(self, *args, **kwargs):
		super(ChildPageForm, self).__init__(*args, **kwargs)

	class Meta:
		model = ChildPage

class ContentBlockForm(forms.ModelForm):
	"""
	modelform contentblock
	"""
	
	def __init__(self, *args, **kwargs):
		super(ContentBlockForm, self).__init__(*args, **kwargs)
		instance = self.instance
		if instance:
			# exclude instance contentblock from ordering itself
			self.fields['show_after'].queryset=ContentBlock.objects.exclude(id=instance.id)

	class Meta:
		model = ContentBlock

		widgets = {

				'content': CKEditorWidget()
		}
