from django import forms
from . import models
from django.contrib.admin.widgets import AdminDateWidget



class AttendanceForms(forms.ModelForm):
    #m_date=forms.DateField(widget=AdminDateWidget)
    m_date = forms.DateField(widget=AdminDateWidget())
    class Meta:
        model = models.Attendances

        fields = ['meeting']
