from django import forms

from employees.models import EmployeeModel


class EmployeeForm(forms.ModelForm):
    model = EmployeeModel
    fields = '__all__'
    widgets = {
        'first_name': forms.TextInput(attrs={
            'placeholder': 'Enter first name'
        }),
        'last_name': forms.TextInput(attrs={
            'placeholder': 'Enter last name'
        }),
        'age': forms.IntegerField(),
        'hourly_wage': forms.IntegerField(),
        'hours_weekly': forms.IntegerField(),
    }