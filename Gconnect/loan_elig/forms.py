from django import forms
from .import models


class LoanEligForms(forms.ModelForm):
    class Meta:
        model = models.LoanEligibility
        fields = ['loan_elig_name']
