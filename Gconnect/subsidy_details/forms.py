from django import forms
from .import models


class SubDetailsForms(forms.ModelForm):
    class Meta:
        model = models.SubsidyDetails
        fields = ['subsidy_typ_name', 'subsidy_elig_name', 'subsidy_prio_name']
