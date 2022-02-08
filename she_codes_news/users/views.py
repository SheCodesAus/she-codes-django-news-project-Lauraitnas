from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views import generic
from .models import CustomUser
from .forms import CustomUserCreationForm
from news.models import NewsStory


class CreateAccountView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/createAccount.html'

class UserPageView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('Profile')
    template_name = 'users/profile.html'



class MyStoryView(generic.ListView):
    model = CustomUser
    template_name = 'users/profile.html'
    context_object_name = 'my_stories'

    # def get_queryset(self):
    #     return NewsStory.objects.filter(author=self.request.user.id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['my_stories'] = NewsStory.objects.filter(author=self.request.user.id)
        return context



