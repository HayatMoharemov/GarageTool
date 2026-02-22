from django.core.validators import MinValueValidator
from django.db import models
from django.utils.text import slugify

from garage.models import CarModel, MotorcycleModel


class EmployeeModel(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField(validators=[MinValueValidator(18)])
    hourly_wage = models.DecimalField(max_digits=5,
                                      decimal_places=2,
                                      validators=[MinValueValidator(0)])
    hours_weekly = models.DecimalField(max_digits=3,
                                       decimal_places=1,
                                       validators=[MinValueValidator(0)])
    hired_at = models.DateField(auto_now_add=True)
    assigned_cars = models.ManyToManyField(CarModel,
                                           blank=True,
                                           related_name='employees_cars')
    assigned_bikes = models.ForeignKey(MotorcycleModel,
                                            null=True,
                                            on_delete=models.SET_NULL,
                                            related_name='employees_bikes')
    slug = models.SlugField(unique=True,
                            editable=False)

    def save(self, *args, **kwargs):
        if not self.slug:
            super().save(*args, **kwargs)
            self.slug = slugify(f"{self.first_name}-{self.last_name}-{self.id}")
            return super().save(update_fields=["slug"])
        return super().save(*args, **kwargs)

    def __str__(self):
        return f"Employee {self.first_name} {self.last_name} with ID {self.id}"