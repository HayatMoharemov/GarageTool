from django.db import models

from common.models import TimeStampModel
from common.validators import check_if_is_positive


class VehicleTypeBaseModel(TimeStampModel):

    class VehicleTypeChoices(models.TextChoices):
        MOTORCYCLE = 'MC', 'Motorcycle'
        CAR = 'CAR', 'Car'

    class VehicleFuelChoices(models.TextChoices):
        PETROL = 'PET', 'Petrol'
        DIESEL = 'DIESEL', 'Diesel'

    type = models.CharField(max_length=15,
                            choices=VehicleTypeChoices.choices)
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    production_date = models.DateField()
    mileage = models.BigIntegerField(validators=[check_if_is_positive])
    engine_displacement = models.DecimalField(max_digits=4,
                                              decimal_places=1,
                                              validators=[check_if_is_positive])
    horsepower = models.IntegerField(validators=[check_if_is_positive])
    fuel_type = models.CharField(max_length=20,
                                 choices=VehicleFuelChoices.choices)
    is_repaired = models.BooleanField(default=False)
    notes = models.TextField()


    class Meta:
        abstract = True
        ordering = ['-created_at']

    def __str__(self):
        displacement = f"{self.engine_displacement}"
        if self.type == self.VehicleTypeChoices.MOTORCYCLE:
            displacement += 'cc'
        else:
            displacement += 'L'

        return f"{self.type} - {self.make} {self.model} {displacement}."

class CarModel(VehicleTypeBaseModel):
    class Meta:
        verbose_name = 'Car'
        verbose_name_plural = 'Cars'

    type = models.CharField(max_length=20,
                            choices=VehicleTypeBaseModel.VehicleTypeChoices.choices,
                            default=VehicleTypeBaseModel.VehicleTypeChoices.CAR,
                            editable=False)

class MotorcycleModel(VehicleTypeBaseModel):
    class Meta:
        verbose_name = 'Motorcycle'
        verbose_name_plural = 'Motorcycles'

    class MotorcycleEngineTypeChoices(models.TextChoices):
        TWOST = '2T', '2-Stroke'
        FOURST = '4T', '4-Stroke'

    type = models.CharField(max_length=20,
                                 choices=VehicleTypeBaseModel.VehicleTypeChoices.choices,
                                 default=VehicleTypeBaseModel.VehicleTypeChoices.MOTORCYCLE,
                                 editable=False)
    engine_type = models.CharField(max_length=15,
                                   choices=MotorcycleEngineTypeChoices.choices)
    fuel_type = models.CharField(max_length=20,
                                 choices=VehicleTypeBaseModel.VehicleFuelChoices.choices,
                                 default=VehicleTypeBaseModel.VehicleFuelChoices.PETROL,
                                 editable=False)

    def save(self, *args, **kwargs):
        self.fuel_type = self.VehicleFuelChoices.PETROL
        super().save(*args, **kwargs)

