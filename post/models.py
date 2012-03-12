from django.db import models
from django.contrib.flatpages.models import FlatPage

class Post(models.Model):
	title 		= models.CharField(max_length=255)
	date_created 	= models.DateField(auto_now_add=True)
	body 		= models.TextField()

	def __unicode__(self):
		return self.title

class ContentBlock(models.Model):
	title = models.CharField(max_length=255)
	
	class Meta:
		abstract = True

class CMSPage(FlatPage):
	order_by = models.ForeignKey('CMSPage', null=True) 

class SubPage(CMSPage):
	cmspage = models.ForeignKey('CMSPage', related_name='sub_page')

class RealPage(FlatPage):
	class Meta:
		proxy = True
