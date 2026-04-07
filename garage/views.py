from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import Http404
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from common.mixins import VehicleObjectMixin
from garage.forms import MotorcycleForm, CarForm
from garage.models import MotorcycleModel, CarModel


class ViewGarage(LoginRequiredMixin, VehicleObjectMixin, ListView):
    template_name = 'garage/view-garage.html'
    context_object_name = 'vehicles'
    paginate_by = 12

    def get_queryset(self):

        qs = self.request.GET.get('q', '')

        vehicles = []

        motorcycles = MotorcycleModel.objects.filter(owner=self.request.user)

        if qs:
            motorcycles = motorcycles.filter(Q(make__icontains=qs) | Q(model__icontains=qs))

        cars = CarModel.objects.filter(owner=self.request.user)

        if qs:
            cars = cars.filter(Q(make__icontains=qs) | Q(model__icontains=qs))

        for c in cars:
            vehicles.append(c)

        for m in motorcycles:
            vehicles.append(m)

        return vehicles

class VehicleCreateBaseView(LoginRequiredMixin, CreateView):

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class AddBike(VehicleCreateBaseView):
    model = MotorcycleModel
    form_class = MotorcycleForm
    template_name = 'garage/add-bike.html'
    success_url = reverse_lazy('garage:view_garage')

class AddCar(VehicleCreateBaseView):
    model = CarModel
    form_class = CarForm
    template_name = 'garage/add-car.html'
    success_url = reverse_lazy('garage:view_garage')

class VehicleDetail(LoginRequiredMixin, VehicleObjectMixin, DetailView):
    template_name = 'garage/vehicle-detail.html'
    slug_field = 'slug'
    slug_url_kwarg = 'vehicle_slug'


class VehicleEdit(LoginRequiredMixin, VehicleObjectMixin, UpdateView):
    template_name = 'garage/update-vehicle.html'
    slug_url_kwarg = 'vehicle_slug'
    slug_field = 'slug'

    def get_form_class(self):
        vehicle = self.get_object()
        if isinstance(vehicle, CarModel):
            return CarForm
        elif isinstance(vehicle, MotorcycleModel):
            return MotorcycleForm


    def get_success_url(self):
        return reverse(
            'garage:vehicle_detail',
                       kwargs={
                           'vehicle_slug': self.object.slug
                       }
        )

class DeleteVehicle(LoginRequiredMixin,VehicleObjectMixin, DeleteView):
    slug_url_kwarg = 'vehicle_slug'
    template_name = 'garage/delete-vehicle.html'
    success_url = reverse_lazy('garage:view_garage')
