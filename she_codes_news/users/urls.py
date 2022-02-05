from django.urls import path
from .views import CreateAccountView, UserPageView

app_name = 'users'

urlpatterns = [
    path('create-account/', CreateAccountView.as_view(),
    name='createAccount'),
    path('profile/', UserPageView.as_view(),
    name='profile'),
]