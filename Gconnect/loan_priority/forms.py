from django import forms
from .import models


class LoanPrioForms(forms.ModelForm):
    class Meta:
        model = models.LoanPriority
        fields = ['loan_prio_name', 'loan_prio_mark']
