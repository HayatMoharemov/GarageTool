from django.db import models

from accounts.models import BusinessUser, GeneralUser
from common.models import TimeStampModel
from garage.models import CarModel, MotorcycleModel


class ContactModel(TimeStampModel):
    name = models.ForeignKey(GeneralUser,
                             related_name='user',
                             on_delete=models.CASCADE)
    company = models.ForeignKey(BusinessUser,
                                related_name='company',
                                on_delete=models.CASCADE)
    car = models.ForeignKey(CarModel,
                                related_name='car',
                                on_delete=models.CASCADE,
                                null=True,
                                blank=True)
    motorcycle = models.ForeignKey(MotorcycleModel,
                                   related_name='motorcycle',
                                   on_delete=models.CASCADE,
                                   null=True,
                                   blank=True)
    description = models.TextField()
