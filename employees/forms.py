from django import forms

from employees.models import EmployeeModel


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = EmployeeModel
        fields = '__all__'
        widgets = {
            'first_name': forms.TextInput(attrs={
                'placeholder': 'Enter first name'
            }),
            'last_name': forms.TextInput(attrs={
                'placeholder': 'Enter last name'
            }),
            'age': forms.NumberInput(
                attrs={
                    'min': 18
            }),
            'hourly_wage': forms.NumberInput(attrs={
                    'min': 0
            }),
            'hours_weekly': forms.NumberInput(attrs={
                    'min': 0
            }),
            'hired_at': forms.DateInput(attrs={
                'type': 'date'
            })
        }