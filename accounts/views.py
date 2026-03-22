from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views import generic as views
from django.shortcuts import render
from django.views.generic import DetailView

from accounts.forms import AccountCreationForm

UserModel = get_user_model()

class AccountRegisterView(views.CreateView):
    model = UserModel
    form_class = AccountCreationForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('account:login')

class AccountLoginView(LoginView):
    template_name = 'accounts/login.html',
    redirect_authenticated_user = True
    next_page = reverse_lazy('common:home')

class AccountDetailView(DetailView):
    model = UserModel
    template_name = 'accounts/profile_details.html'
    context_object_name = 'user_profile'

    def get_object(self, queryset=None):
        return self.request.user