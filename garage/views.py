from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from garage.forms import MotorcycleForm, CarForm
from garage.models import MotorcycleModel, CarModel


class ViewGarage(ListView):
    template_name = 'garage/view-garage.html'
    context = 'vehicles'

    def get_queryset(self):
        vehicles = []

        motorcycles = MotorcycleModel.objects.all()
        cars = CarModel.objects.all()

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
