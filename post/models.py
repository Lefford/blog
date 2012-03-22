from django.db import models
from django.contrib import admin
from django.contrib.flatpages.models import FlatPage
from django import forms
from django.contrib.sites.models import Site

class BasePage(models.Model):
	url 			= models.CharField(max_length=100, db_index=True)
	title 			= models.CharField(max_length=255, blank=True)
	template_name 		= models.CharField(max_length=70, blank=True)
	registration_required 	= models.BooleanField()
	#breadcrumb 		= models.CharField(max_length=20, blank=True)	

	class Meta:
		abstract = True

class Post(models.Model):
	title 		= models.CharField(max_length=255)
	date_created 	= models.DateField(auto_now_add=True)
	body 		= models.TextField()

	def __unicode__(self):
		return '{0} -- {1}'.format(self.url, self.title)
	
	class Meta:
		abstract = True

class BaseContentBlock(models.Model):
	title 			= models.CharField(max_length=30)
	content 		= models.TextField()

	class Meta:
		abstract = True

class ContentBlock(BaseContentBlock):
	
	show_after 		= models.ForeignKey('ContentBlock', blank=True, null=True, related_name='content_predecessor')

	def __unicode__(self):
		return '{0} - {1}'.format(self.id, self.title)

class ParentPage(BasePage):
	"""
	Parent page 
	"""

	show_after 		= models.ForeignKey('ParentPage', blank=True, null=True, related_name='page_predecessor')
	sites 			= models.ManyToManyField(Site)

	def __unicode__(self):
		return self.title
	
class ChildPage(BasePage):
	"""
	Child page
	"""

	parent_page 		= models.ForeignKey('ParentPage')

	def __unicode__(self):
		return self.title

class Post(models.Model):
	"""
	Entry
	"""

	title 			= models.CharField(max_length=255)
	date_created 		= models.DateField(auto_now_add=True)
	body 			= models.TextField()

	def __unicode__(self):
		return self.title
class CMSPage(FlatPage):
	order_by = models.ForeignKey('CMSPage', null=True) 

class SubPage(CMSPage):
	cmspage = models.ForeignKey('CMSPage', related_name='sub_page')

class RealPage(FlatPage):
	class Meta:
		proxy = True
