from django.db import models
from post.forms import FlatPageForm

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
