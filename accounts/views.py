from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, ListView

from accounts.forms import AccountCreationForm, BusinessProfileForm, IndividualProfileForm
from accounts.models import BusinessUser, GeneralUser, IndividualUser
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
        user = self.request.user

        if user.is_business:
            return get_object_or_404(BusinessUser.objects.select_related('user'), user=user)

        try:
            return user.individualuser
        except IndividualUser.DoesNotExist:
            raise Http404("No individual profile found for this user. Please contact support.")

    def form_valid(self, form):
        return super().form_valid(form)

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

class CompanyListView(ListView):
    model = BusinessUser
    template_name = 'accounts/companies_list.html'
    context_object_name = 'companies'
    paginate_by = 10

    def get_queryset(self):

        qs = self.request.GET.get('q', '')

        companies = []

        company = BusinessUser.objects.filter(company_name__icontains=qs)

        for c in company:
            companies.append(c)

        return companies

class CompanyDetailView(DetailView):
    template_name = 'accounts/company_details.html'
    slug_field = 'slug'
    slug_url_kwarg = 'company_slug'

    def get_object(self, queryset=None):
        slug = self.kwargs.get('company_slug')

        company = BusinessUser.objects.filter(slug=slug).first()
        if company:
            return company

        raise Http404('No such company!')
