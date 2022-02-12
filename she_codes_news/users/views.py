from django.shortcuts import redirect
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

class UserPageView(generic.DetailView):
    model = CustomUser
    template_name = 'users/profile.html'
    context_object_name = 'my_stories'

    # def get_queryset(self):
    #     return NewsStory.objects.filter(author=self.request.user.id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['my_stories'] = NewsStory.objects.filter(author=self.request.user.id)
        return context

    
def login_redirect(request):
    return redirect (reverse_lazy('users:profile', kwargs={'pk': request.user.id}))


    # def get(self, request, *args, **kwargs):
    #     if 'pk' not in kwargs:
    #         kwargs['pk'] = request.user.id
    #     # self.object = self.get_object()
    #     # context = self.get_context_data(object=self.object)
    #     return super().get(request, *args, **kwargs)


