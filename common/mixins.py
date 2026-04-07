from django.contrib.auth.mixins import UserPassesTestMixin
from django.core.exceptions import PermissionDenied
from django.http import Http404

from garage.models import CarModel, MotorcycleModel


class ReadOnlyFieldMixin:

    read_only_fields = []

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in self.read_only_fields:
            if field_name in self.fields:
                self.fields[field_name].disabled = True

class AccountOwnershipCheckMixin(UserPassesTestMixin):

    def test_func(self):
        obj = self.get_object()

        if hasattr(obj, 'user'):
            return obj.user == self.request.user

        if hasattr(obj, 'is_business') or obj.__class__.__name__ == 'GeneralUser':
            return obj == self.request.user

        return False

    def handle_no_permission(self):
        raise PermissionDenied("You do not have permission to edit this profile.")


class VehicleObjectMixin:
    slug_url_kwarg = 'vehicle_slug'

    def get_object(self, queryset=None):
        slug = self.kwargs.get(self.slug_url_kwarg)

        car = CarModel.objects.filter(
            slug=slug,
            owner=self.request.user
        ).first()

        if car:
            return car

        motorcycle = MotorcycleModel.objects.filter(
            slug=slug,
            owner=self.request.user
        ).first()

        if motorcycle:
            return motorcycle

        raise Http404("Vehicle not found")