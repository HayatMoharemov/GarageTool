from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.text import slugify

from accounts.managers import CustomGeneralUserManager
from common.models import TimeStampModel
from common.validators import check_phone_number


class GeneralUser(AbstractUser, TimeStampModel):

    class UserTypeChoices(models.TextChoices):
        BUSINESS = 'BU', 'Business User'
        INDIVIDUAL = 'IU', 'Individual User'

    type = models.CharField(max_length=2,
                            choices=UserTypeChoices.choices)
    email = models.EmailField(unique=True)

    objects = CustomGeneralUserManager()

    username = None
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    @property
    def is_business(self):
        return self.type == self.UserTypeChoices.BUSINESS

    @property
    def is_individual(self):
        return self.type == self.UserTypeChoices.INDIVIDUAL


class BusinessUser(models.Model):
    class Meta:
        verbose_name = 'Business Profile'
        verbose_name_plural = 'Business Profiles'
    user = models.OneToOneField(GeneralUser,
                                on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100,
                                    unique=True)
    tax_number = models.CharField(max_length=50,
                                  unique=True)
    slug = models.SlugField(unique=True,
                            editable=False)

    def save(self, *args, **kwargs):
        is_new = self.pk is None
        super().save(*args, **kwargs)

        if not self.company_name:
            if not self.slug or self.slug != str(self.pk):
                self.slug = str(self.pk)
                super().save(update_fields=['slug'])

        else:
            new_slug = f"{slugify(self.company_name)}-{self.pk}"
            if self.slug != new_slug:
                self.slug = new_slug
                super().save(update_fields=['slug'])

    def __str__(self):
        return f"{self.user.email} - {self.user.get_type_display()} created on {self.user.created_at}"


class IndividualUser(models.Model):
    class Meta:
        verbose_name = 'Individual Profile'
        verbose_name_plural = 'Individual Profiles'

    user = models.OneToOneField(GeneralUser,
                                on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=16,
                                    validators=[check_phone_number])

    def __str__(self):
        return f"{self.user.email} - {self.user.get_type_display()} created on {self.user.created_at}"
