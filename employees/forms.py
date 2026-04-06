from django import forms

from employees.models import EmployeeModel
from garage.models import CarModel, MotorcycleModel


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = EmployeeModel
        exclude = ['company', 'slug']
        widgets = {
            'first_name': forms.TextInput(attrs={
                'placeholder': 'Enter employee first name'
            }),
            'last_name': forms.TextInput(attrs={
                'placeholder': 'Enter employee last name'
            }),
            'age': forms.NumberInput(attrs={
                'placeholder':'Enter employee age'
                ,'min': 18
            }),
            'hourly_wage': forms.NumberInput(attrs={
                'placeholder':'Enter hourly wage',
                'min': 0
            }),
            'hours_weekly': forms.NumberInput(attrs={
                'min': 0,
                'placeholder':'Enter weekly working hours'
            }),
            'hired_at': forms.DateInput(attrs={
                'type': 'date'
            })
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user and hasattr(user, 'businessuser'):
            self.fields['assigned_cars'].queryset = CarModel.objects.filter(owner=user)
            self.fields['assigned_bikes'].queryset = MotorcycleModel.objects.filter(owner=user)