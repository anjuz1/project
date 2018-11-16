from django import forms
from . import models
from django.contrib.admin.widgets import AdminDateWidget



class GmeetingForms(forms.ModelForm):
    #m_date=forms.DateField(widget=AdminDateWidget)
    tdate = forms.DateField(widget=AdminDateWidget())
    class Meta:
        model = models.Gmeeting

        fields = ['decisions']
