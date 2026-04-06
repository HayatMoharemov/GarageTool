from django.core.validators import MinValueValidator
from django.db import models
from django.utils.text import slugify

from accounts.models import BusinessUser
from common.validators import check_if_is_alpha
from garage.models import CarModel, MotorcycleModel


class EmployeeModel(models.Model):

    class Meta:
        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'

    company = models.ForeignKey(BusinessUser,
                                on_delete=models.CASCADE,
                                related_name="employees")

    first_name = models.CharField(max_length=50,
                                  validators=[check_if_is_alpha])
    last_name = models.CharField(max_length=50,
                                  validators=[check_if_is_alpha])
    age = models.IntegerField(validators=[MinValueValidator(18)],
                              error_messages={'min_value':'Employees must be at least 18 years old.'})
    hourly_wage = models.DecimalField(max_digits=5,
                                      decimal_places=2,
                                      validators=[MinValueValidator(0)],
                                      error_messages={'min_value':'Hourly wage cannot be less than 0'})
    hours_weekly = models.DecimalField(max_digits=3,
                                       decimal_places=1,
                                       validators=[MinValueValidator(0)],
                                       error_messages={'min_value':'Working hours cannot be less than 0'})
    hired_at = models.DateField()
    assigned_cars = models.ManyToManyField(CarModel,
                                           blank=True,
                                           related_name='employees_cars',
                                           default=None)
    assigned_bikes = models.ForeignKey(MotorcycleModel,
                                        blank=True,
                                        null=True,
                                        on_delete=models.SET_NULL,
                                        related_name='employees_bikes',
                                       default=None)
    slug = models.SlugField(unique=True,
                            editable=False)

    def save(self, *args, **kwargs):
        if not self.slug:
            super().save(*args, **kwargs)
            self.slug = slugify(f"{self.first_name}-{self.last_name}-{self.id}-{self.company.company_name}")
            return super().save(update_fields=["slug"])
        return super().save(*args, **kwargs)

    def __str__(self):
        return f"Employee {self.first_name} {self.last_name} with ID {self.id} working at {self.company.company_name}"