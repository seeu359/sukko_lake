from django import forms

from sukko_lake.models import Application


class CreateApplicationForm(forms.ModelForm):

    class Meta:
        model = Application
        fields = (
            'client_name',
            'client_number',
        )
        widgets = {
            'client_name': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Ваше имя'}
            ),
            'client_number': forms.TextInput(
                attrs={
                    'class': 'form-control', 'placeholder': 'Номер телефона'
                }
            ),
        }
