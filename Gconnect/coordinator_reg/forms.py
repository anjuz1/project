from django import forms
from . import models


class CoordRegForms(forms.ModelForm):
    confirm_pwd = forms.CharField(
        required=True,
        label='Username',
        max_length=32,
        widget=forms.PasswordInput()
    )
    coord_pwd = forms.CharField(
        required=True,
        label='password',
        max_length=32,
        widget=forms.PasswordInput()
    )

    class Meta:
        model = models.CoordRegistration
        fields = ['coord_name', 'coord_hname', 'coord_po', 'coord_place', 'coord_phno', 'coord_mailid', 'coord_gender',
                  'coord_dob', 'coord_uname', 'coord_pwd']
