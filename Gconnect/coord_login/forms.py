from django import forms
from coordinator_reg.models import CoordRegistration


class LoginForms(forms.Form):
    username = forms.CharField(
        required=True,
        label='Username',
        max_length=32
    )
    password = forms.CharField(
        required=True,
        label='Password',
        max_length=32,
        widget=forms.PasswordInput()
    )

    class Meta:
        model = CoordRegistration
        fields = ['wardmemb_name']
