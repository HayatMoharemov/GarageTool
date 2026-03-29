from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView

from accounts.forms import AccountCreationForm, BusinessProfileForm, IndividualProfileForm
from accounts.models import BusinessUser,GeneralUser
from common.mixins import AccountOwnershipCheckMixin

UserModel = get_user_model()

class AccountRegisterView(CreateView):
    model = UserModel
    form_class = AccountCreationForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('accounts:login')


class AccountDetailView(DetailView):
    model = UserModel
    template_name = 'accounts/profile_details.html'
    context_object_name = 'user_profile'

    def get_object(self, queryset=None):
        if self.request.user.is_business:
            return get_object_or_404(
                GeneralUser.objects.select_related('businessuser'),
                pk=self.request.user.pk
            )
        return self.request.user

class ProfileEditView(LoginRequiredMixin, AccountOwnershipCheckMixin, UpdateView):
    template_name = 'accounts/edit_profile.html'

    def get_form_class(self):
        if self.request.user.is_business:
            return BusinessProfileForm
        return IndividualProfileForm

    def get_object(self, queryset=None):
        if self.request.user.is_business:
            return get_object_or_404(BusinessUser, user=self.request.user)
        return self.request.user

    def form_valid(self, form):
        self.object = form.save()
        return redirect(self.get_success_url())

    def get_success_url(self):
        return reverse_lazy('accounts:details',
                            kwargs={'pk': self.request.user.pk})
class AccountDeleteView(LoginRequiredMixin, AccountOwnershipCheckMixin, DeleteView):
    model = UserModel
    template_name = 'accounts/delete_profile.html'
    success_url = reverse_lazy('accounts:login')
    context_object_name = 'user_profile'

    def get_object(self, queryset=None):
        return self.request.user