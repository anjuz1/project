from django import forms
from . import models


class ChitDetailsForm(forms.ModelForm):
    class Meta:
        model = models.ChitDetails
        fields = ['chit_name', 'members_name', 'chit_details_date']
