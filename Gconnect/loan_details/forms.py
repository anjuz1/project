from django import forms
from .import models


class LoanDetailsForms(forms.ModelForm):
    class Meta:
        model = models.LoanDetails
        fields = ['loan_elig_name', 'loan_prio_name']
