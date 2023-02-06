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