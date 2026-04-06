from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from accounts.models import BusinessUser, IndividualUser


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

class IndividualProfileForm(forms.ModelForm):
    first_name = forms.CharField(max_length=150, required=True, label="First Name")
    last_name = forms.CharField(max_length=150, required=True, label="Last Name")

    class Meta:
        model = IndividualUser
        fields = ['first_name', 'last_name', 'phone_number']

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        if self.instance and hasattr(self.instance, 'user') and self.instance.user:
            self.fields['first_name'].initial = self.instance.user.first_name
            self.fields['last_name'].initial = self.instance.user.last_name

    def save(self, commit=True):
        profile = super().save(commit=False)
        user = profile.user

        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']

        user.save()

        if commit:
            profile.save()
        return profile


class BusinessProfileForm(forms.ModelForm):
    class Meta:
        model = BusinessUser
        fields = ['company_name', 'tax_number']

