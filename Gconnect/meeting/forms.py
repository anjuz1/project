from django import forms
from .import models


class MeetingForms(forms.ModelForm):
    class Meta:
        model = models.Meeting
        fields = ['place_name', 'meeting_date', 'meeting_time', 'meeting_agenda']
