from django.db.models import Q
from django.http import Http404
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView, CreateView

from catalogue.forms import ServiceForm
from catalogue.models import PartModel, ServiceModel

class CatalogueLanding(TemplateView):
    template_name = 'catalogue/catalogue-landing.html'

class ServicesDetails(DetailView):
    template_name = 'catalogue/services-details.html'
    slug_field = 'slug'
    slug_url_kwarg = 'services_slug'

    def get_object(self, queryset=None):
        slug = self.kwargs.get('services_slug')

        service = ServiceModel.objects.filter(slug=slug).first()

        if service:
            return service

        raise Http404('Service not found')

class ServicesList(ListView):
    template_name = 'catalogue/services-list.html'
    context_object_name = 'services'
    paginate_by = 10

    def get_queryset(self):
        qs = self.request.GET.get('q', '')

        part = ServiceModel.objects.all()

        if qs:
            part = part.filter(Q(title__icontains=qs) | Q(manufacturer__icontains=qs))

        return part

class PartsList(ListView):
    template_name = 'catalogue/parts-list.html'
    context_object_name = 'parts'
    paginate_by = 10

    def get_queryset(self):

        qs = self.request.GET.get('q','')

        part = PartModel.objects.all()

        if qs:
            part = part.filter(Q(title__icontains=qs))

        return part


class PartsDetails(DetailView):
    template_name = 'catalogue/part-details.html'
    slug_field = 'slug'
    slug_url_kwarg = 'parts_slug'

    def get_object(self, queryset=None):

        slug = self.kwargs.get('parts_slug')

        part = PartModel.objects.filter(slug=slug).first()

        if part:
            return part

        raise Http404('Part not found')

class AddService(CreateView):
    model = ServiceModel
    form_class = ServiceForm
    template_name = 'catalogue/add-service.html'
    success_url = reverse_lazy('catalogue:services_list')
