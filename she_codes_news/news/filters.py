# from unicodedata import category
import django_filters
from .models import *

class StoryFilter(django_filters.FilterSet):
    # title = django_filters.CharFilter(lookup_expr='icontains')
    # category = django_filters.CharFilter(lookup_expr='icontains')
	
    class Meta:
        model = NewsStory
        fields = '__all__'