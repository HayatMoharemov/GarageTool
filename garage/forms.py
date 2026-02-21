from django import forms

from common.mixins import ReadOnlyFieldMixin
from garage.models import CarModel, VehicleTypeBaseModel, MotorcycleModel


class BaseForm(forms.ModelForm):
    class Meta:
        model = VehicleTypeBaseModel
        fields = '__all__'
        exclude = ['is_repaired']
        widgets = {
            'make': forms.TextInput(attrs={'placeholder': 'Enter make'}),
            'model': forms.TextInput(attrs={'placeholder': 'Enter model'}),
            'production_date': forms.DateInput(attrs={'type': 'date'}),
            'engine_displacement': forms.NumberInput(attrs={'min': 0}),
            'mileage': forms.NumberInput(attrs={'placeholder': 'Enter mileage',
                                                'min': 0}),
            'horsepower': forms.NumberInput(attrs={'placeholder': 'Enter horsepower',
                                                   'min': 0}),
            'notes': forms.Textarea(attrs={'placeholder': 'Add notes to the vehicle'})
        }

class CarForm(BaseForm):
    class Meta(BaseForm.Meta):
        model = CarModel

class MotorcycleForm(ReadOnlyFieldMixin, BaseForm):
    read_only_fields = ['fuel_type']

    class Meta(BaseForm.Meta):
        model = MotorcycleModel

