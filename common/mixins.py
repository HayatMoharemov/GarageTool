from django.contrib.auth.mixins import UserPassesTestMixin
from django.core.exceptions import PermissionDenied


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
