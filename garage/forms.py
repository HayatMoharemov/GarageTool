from django import forms

from common.mixins import ReadOnlyFieldMixin
from garage.models import CarModel, VehicleTypeBaseModel, MotorcycleModel


class BaseForm(forms.ModelForm):
    class Meta:
        model = VehicleTypeBaseModel
        fields = '__all__'
        widgets = {
            'make': forms.TextInput(attrs={'placeholder': 'Enter make'}),
            'model': forms.TextInput(attrs={'placeholder': 'Enter model'}),
            'mileage': forms.NumberInput(attrs={'placeholder': 'Enter mileage'}),
            'horsepower': forms.NumberInput(attrs={'placeholder': 'Enter horsepower'}),
            'notes': forms.Textarea(attrs={'placeholder': 'Add notes to the vehicle'})
        }

class CarForm(BaseForm):
    class Meta(BaseForm.Meta):
        model = CarModel

class MotorcycleForm(ReadOnlyFieldMixin, BaseForm):
    read_only_fields = ['fuel_type']

    class Meta(BaseForm.Meta):
        model = MotorcycleModel

