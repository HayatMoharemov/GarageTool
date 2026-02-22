from django.db import models

from catalogue.models import PartModel, ServiceModel


class CalculatorModel(models.Model):
    car = models.ForeignKey(
        'garage.CarModel',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    motorcycle = models.ForeignKey(
        'garage.MotorcycleModel',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    parts = models.ManyToManyField(PartModel, blank=True)
    services = models.ManyToManyField(ServiceModel, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def vehicle(self):
        if self.car:
            return self.car
        else:
            return self.motorcycle

    @property
    def total_price(self):
        parts_total = sum(part.price for part in self.parts.all())
        services_total = sum(service.price for service in self.services.all())

        return parts_total + services_total

    def __str__(self):
        return f"Offer for {self.vehicle}"
