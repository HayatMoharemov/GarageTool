from django import forms

from catalogue.models import ServiceModel


class ServiceForm(forms.ModelForm):

    class Meta:
        model = ServiceModel
        exclude = ['slug']
