from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views import generic
from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm
from news.models import NewsStory
from django.core.exceptions import PermissionDenied



class CreateAccountView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/createAccount.html'

class EditAccountView(generic.UpdateView):
    model = CustomUser
    fields = ['first_name', 'last_name', 'email', 'profile_picture', 'bio', 'github', 'linkedin']
    success_url = reverse_lazy('users:my_profile')
    # context_object_name = "user"
    template_name = 'users/editUser.html'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj != self.request.user:
            raise PermissionDenied
        return obj


class UserPageView(generic.DetailView):
    model = CustomUser
    template_name = 'users/profile.html'
    # context_object_name = 'my_stories'


    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['my_stories'] = NewsStory.objects.filter(author=self.request.user.id)
    #     return context

    
def login_redirect(request):
    return redirect (reverse_lazy('users:profile', kwargs={'pk': request.user.id}))



