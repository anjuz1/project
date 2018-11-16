from django import forms
from .import models


class SubTypeForms(forms.ModelForm):
    class Meta:
        model = models.SubsidyTypes
        fields = ['subsidy_type_name', 'subsidy_type_sub_perc', 'subsidy_type_self_perc']
