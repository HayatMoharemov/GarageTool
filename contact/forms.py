from django import forms

from contact.models import ContactModel


class ContactForm(forms.ModelForm):

    class Meta:

        model = ContactModel
        fields = ['car', 'motorcycle', 'description']
        widgets = {
            'description': forms.Textarea(
                attrs={
                    'placeholder':'Please describe your request here'
                }
            )
        }

    def __init__(self, *args, user=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user

        if user and user.is_authenticated:

            self.fields['car'].queryset = user.carmodel_vehicles.all()
            self.fields['motorcycle'].queryset = user.motorcyclemodel_vehicles.all()

            if not self.fields['car'].queryset.exists():
                self.fields.pop('car')

            if not self.fields['motorcycle'].queryset.exists():
                self.fields.pop('motorcycle')
