from django import forms
from .import models


class ChitForms(forms.ModelForm):
    class Meta:
        model = models.Chit
        fields = ['chit_amount', 'chit_start_date', 'chit_name']
