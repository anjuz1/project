from django import forms
from .import models


class PlaceForms(forms.ModelForm):
    class Meta:
        model = models.Place
        fields = ['name']
