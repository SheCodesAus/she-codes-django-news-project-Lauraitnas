# from xml.etree.ElementTree import Comment
from django.contrib import admin
from .models import Category, NewsStory, Comment

admin.site.register(Category)
admin.site.register(NewsStory)
# Register your models here.
admin.site.register(Comment)