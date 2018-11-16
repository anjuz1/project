from django import forms
from . import models


class HouseNameForms(forms.ModelForm):
    class Meta:
        model = models.Housename
        fields = ['house_name', 'house_num', 'house_po', 'house_street', 'house_district', 'house_state', 'house_adhar', 'house_uname', 'house_pwd', 'house_mail']
