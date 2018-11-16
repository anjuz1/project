from django import forms
from coordinator_reg.models import CoordRegistration


class CoordProfForms(forms.ModelForm):
    confirm_pwd = forms.CharField(
        required=True,
        label='Username',
        max_length=32,
        widget=forms.PasswordInput()
    )

    class Meta:
        model = CoordRegistration
        fields = ['coord_name', 'coord_hname', 'coord_po', 'coord_place', 'coord_phno', 'coord_mailid', 'coord_gender',
                  'coord_dob', 'coord_uname', 'coord_pwd']
