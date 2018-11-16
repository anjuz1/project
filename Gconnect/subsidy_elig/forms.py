from django import forms
from .import models


class SubEligForms(forms.ModelForm):
    class Meta:
        model = models.SubsidyEligibility
        fields = ['subsidy_elig_name','subsidy_ftype']
