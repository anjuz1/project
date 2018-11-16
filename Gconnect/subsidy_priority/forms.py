from django import forms
from .import models


class SubPrioForms(forms.ModelForm):
    class Meta:
        model = models.SubsidyPriority
        fields = ['subsidy_prio_name', 'subsidy_prio_mark']
        #'subsidy_ptype', 'subsidy_pelig',
