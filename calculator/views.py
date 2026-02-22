from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from calculator.models import CalculatorModel
from catalogue.models import PartModel, ServiceModel
from garage.models import CarModel, MotorcycleModel


def create_offer(request: HttpRequest) -> HttpResponse:
    cars = CarModel.objects.all()
    motorcycles = MotorcycleModel.objects.all()
    parts = PartModel.objects.all()
    services = ServiceModel.objects.all()

    if request.method == "POST":
        vehicle_data = request.POST.get("vehicle")

        selected_parts = request.POST.getlist("parts")
        selected_services = request.POST.getlist("services")

        calculator = CalculatorModel.objects.create()

        if vehicle_data:
            vehicle_type, vehicle_id = vehicle_data.split("-")

            if vehicle_type == "car":
                calculator.car_id = vehicle_id
            elif vehicle_type == "motorcycle":
                calculator.motorcycle_id = vehicle_id

        calculator.save()

        calculator.parts.set(selected_parts)
        calculator.services.set(selected_services)

        return redirect("calculator:offer", pk=calculator.pk)

    context = {
        "cars": cars,
        "motorcycles": motorcycles,
        "parts": parts,
        "services": services,
    }

    return render(request,'calculator/create-offer.html', context)

def offer(request:HttpRequest, pk) -> HttpResponse:
    calculator = get_object_or_404(CalculatorModel, pk=pk)
    context = {
        "calculator": calculator
    }
    return render(request, "calculator/offer.html", context)