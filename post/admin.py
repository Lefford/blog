from django.contrib import admin
from post.models import ParentPage, ChildPage, Post, ContentBlock
from post.forms import ParentPageForm, ChildPageForm, ContentBlockForm

class ParentPageAdmin(admin.ModelAdmin):
	form = ParentPageForm

class ChildPageAdmin(admin.ModelAdmin):
	form = ChildPageForm 

class PostAdmin(admin.ModelAdmin):
	pass

class ContentBlockAdmin(admin.ModelAdmin):
	form = ContentBlockForm

admin.site.register(ParentPage, ParentPageAdmin)
admin.site.register(ChildPage, ChildPageAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(ContentBlock, ContentBlockAdmin)
