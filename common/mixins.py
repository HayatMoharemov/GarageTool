from django.contrib.auth.mixins import UserPassesTestMixin


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
            obj = obj.user
        return self.request.user == obj
