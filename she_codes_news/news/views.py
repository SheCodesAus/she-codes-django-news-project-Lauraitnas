from re import template
from django.views import generic
from django.urls import reverse_lazy
from .models import NewsStory
from .forms import StoryForm
from users.models import CustomUser
from django.core.exceptions import PermissionDenied
from django.views.generic.edit import UpdateView
from django.shortcuts import redirect
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin





class IndexView(generic.ListView):
    template_name = 'news/index.html'

    def get_queryset(self):
        '''Return all news stories.'''
        return NewsStory.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_stories'] = NewsStory.objects.all()[:3]
        context['all_stories'] = NewsStory.objects.all()[:20]
        return context


class StoryView(generic.DetailView):
    model = NewsStory
    template_name = 'news/story.html'
    context_object_name = 'story'


class AddStoryView(LoginRequiredMixin,generic.CreateView):
    form_class = StoryForm
    context_object_name = 'storyForm'
    template_name = 'news/createStory.html'
    success_url = reverse_lazy('news:index')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
        


class DeleteStoryView(generic.DeleteView):
    model = NewsStory
    template_name = "news/deleteStory.html"
    context_object_name = "story"
    success_url = reverse_lazy('news:index')

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.author != self.request.user:
            raise PermissionDenied
        return obj


class EditStoryView(generic.UpdateView):
    model = NewsStory
    fields = ['title', 'pub_date', 'url', 'content']
    template_name = "news/editStory.html"
    context_object_name = "story"
    success_url = reverse_lazy('news:index')

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.author != self.request.user:
            raise PermissionDenied
        return obj
