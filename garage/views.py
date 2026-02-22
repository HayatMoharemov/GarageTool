from django.db.models import Q
from django.http import Http404
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from garage.forms import MotorcycleForm, CarForm
from garage.models import MotorcycleModel, CarModel


class ViewGarage(ListView):
    template_name = 'garage/view-garage.html'
    context_object_name = 'vehicles'
    paginate_by = 10

    def get_queryset(self):

        qs = self.request.GET.get('?q', '')

        vehicles = []

        motorcycles = MotorcycleModel.objects.all()
        if qs:
            motorcycles = motorcycles.filter(Q(make__icontains=qs) | Q(model__icontains=qs))
        cars = CarModel.objects.all()
        if qs:
            cars = cars.filter(Q(make__icontains=qs) | Q(model__icontains=qs))

        for c in cars:
            vehicles.append(c)

        for m in motorcycles:
            vehicles.append(m)

        return vehicles

class AddBike(CreateView):
    model = MotorcycleModel
    form_class = MotorcycleForm
    template_name = 'garage/add-bike.html'
    success_url = reverse_lazy('garage:view_garage')

class AddCar(CreateView):
    model = CarModel
    form_class = CarForm
    template_name = 'garage/add-car.html'
    success_url = reverse_lazy('garage:view_garage')

class VehicleDetail(DetailView):
    template_name = 'garage/vehicle-detail.html'
    slug_field = 'slug'
    slug_url_kwarg = 'vehicle_slug'

    def get_object(self, queryset=None):
        slug = self.kwargs.get('vehicle_slug')

        car = CarModel.objects.filter(slug=slug).first()
        if car:
            return car

        motorcycle = MotorcycleModel.objects.filter(slug=slug).first()
        if motorcycle:
            return motorcycle

        raise Http404('Invalid vehicle type')

class VehicleEdit(UpdateView):
    template_name = 'garage/update-vehicle.html'
    slug_url_kwarg = 'vehicle_slug'
    slug_field = 'slug'

    def get_form_class(self):
        vehicle = self.get_object()
        if isinstance(vehicle, CarModel):
            return CarForm
        elif isinstance(vehicle, MotorcycleModel):
            return MotorcycleForm

    def get_object(self, queryset = None):
        slug = self.kwargs.get(self.slug_url_kwarg)

        car = CarModel.objects.filter(slug=slug).first()
        if car:
            return car

        motorcycle = MotorcycleModel.objects.filter(slug=slug).first()
        if motorcycle:
            return motorcycle

        raise Http404('Vehicle not found')

    def get_success_url(self):
        return reverse(
            'garage:vehicle_detail',
                       kwargs={
                           'vehicle_slug': self.object.slug
                       }
        )

class DeleteVehicle(DeleteView):
    slug_url_kwarg = 'vehicle_slug'
    template_name = 'garage/delete-vehicle.html'
    success_url = reverse_lazy('garage:view_garage')

    def get_object(self, queryset=None):
        slug = self.kwargs.get(self.slug_url_kwarg)

        car = CarModel.objects.filter(slug=slug).first()
        if car:
            return car

        motorcycle = MotorcycleModel.objects.filter(slug=slug).first()
        if motorcycle:
            return motorcycle

        raise Http404('No such vehicle found')