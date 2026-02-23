from django import forms

from employees.models import EmployeeModel


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = EmployeeModel
        fields = '__all__'
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