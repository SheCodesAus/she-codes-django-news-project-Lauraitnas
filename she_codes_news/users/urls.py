from django.urls import path
from .views import CreateAccountView, UserPageView, login_redirect

app_name = 'users'

urlpatterns = [
    path('create-account/', CreateAccountView.as_view(), name='createAccount'),
    path('<int:pk>/profile/', UserPageView.as_view(), name='profile'),
    path('profile/', login_redirect, name='my_profile'),
]