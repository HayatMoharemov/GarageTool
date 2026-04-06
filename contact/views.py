from copy import deepcopy

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.dispatch import receiver
from django.shortcuts import get_object_or_404, redirect
from django.utils.text import slugify
from django.views import View
from django.views.generic import CreateView, ListView, DeleteView
from rest_framework.reverse import reverse_lazy

from accounts.models import BusinessUser
from contact.forms import ContactForm
from contact.models import ContactModel



class ContactRequestView(LoginRequiredMixin, CreateView):
    model = ContactModel
    form_class = ContactForm
    template_name = 'contact/contact_form.html'


    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def dispatch(self, request, *args, **kwargs):
        self.company = get_object_or_404(BusinessUser, slug=self.kwargs.get('company_slug'))
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):

        form.instance.sender = self.request.user
        form.instance.name = self.request.user

        company_slug = self.kwargs.get('company_slug')
        try:
            business = BusinessUser.objects.get(slug=company_slug)
            form.instance.receiver = business.user
            form.instance.company = business
        except BusinessUser.DoesNotExist:
            form.instance.receiver = None

        messages.success(self.request, "Your message has been sent successfully!")
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('accounts:company_details',
                            kwargs={'company_slug': self.kwargs.get('company_slug')})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context['company'] = BusinessUser.objects.get(slug=self.kwargs.get('company_slug'))
        except BusinessUser.DoesNotExist:
            context['company'] = None
        return context

class ContactInquiriesView(ListView):
    model = ContactModel
    template_name = 'contact/inquiries.html'
    context_object_name = 'inquiries'
    paginate_by = 10

    def get_queryset(self):

        try:
            business = self.request.user.businessuser
            return ContactModel.objects.filter(company=business)
        except BusinessUser.DoesNotExist:
            return ContactModel.objects.none()

class DeleteInquiry(DeleteView):
    model = ContactModel
    success_url = reverse_lazy('contact:inquiries')
    pk_url_kwarg = 'pk'

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


class AcceptOfferFromInquiry(LoginRequiredMixin, View):

    def post(self, request, pk, *args, **kwargs):

        inquiry = get_object_or_404(ContactModel, pk=pk)
        vehicle = None

        if inquiry.car:
            vehicle = inquiry.car
        elif inquiry.motorcycle:
            vehicle = inquiry.motorcycle


        if vehicle:

            vehicle_copy = deepcopy(vehicle)

            vehicle_copy.pk = None
            vehicle_copy.owner = request.user

            vehicle_copy.description = inquiry.description
            vehicle_copy.slug = f"{slugify(vehicle_copy.slug)}-{request.user.id}"
            vehicle_copy.save()

            inquiry.delete()

            messages.success(request, "Customer vehicle added successfully to your garage!")

        else:
            messages.warning(request, "This inquiry has no vehicle to add.")

        return redirect('garage:view_garage')
