from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from accounts.models import BusinessUser, GeneralUser


class AccountCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('email','type', 'password1', 'password2')
        widgets = {
            'email': forms.EmailInput(attrs={
                'placeholder': 'e.g johncooper@gmail.com'
            }),
            'password1': forms.PasswordInput(attrs={
               'placeholder': 'Password'
            }),
            'password2': forms.PasswordInput(attrs={
                'placeholder': 'Repeat Password'
            }),
        }

class BusinessProfileForm(forms.ModelForm):

    class Meta:
        model = BusinessUser
        fields = ['company_name', 'tax_number']

class IndividualProfileForm(forms.ModelForm):

    class Meta:
        model = GeneralUser
        fields = ['email', 'first_name', 'last_name']