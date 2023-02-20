from django import forms
from django.forms import ModelForm

from .models import (
    Doc
)


class DocForm(ModelForm):
    prefix = "Doc"

    class Meta:
        model = Doc
        fields = "__all__"

        # fields = ['date', 'description']

        # widgets = {
        #     'date': forms.DateInput(
        #         format=('%d.%m.%Y'),
        #         attrs={'class': 'form-control', 
        #                'placeholder': 'Select a date',
        #                'type': 'date'  # <--- IF I REMOVE THIS LINE, THE INITIAL VALUE IS DISPLAYED
        #               })
        # }