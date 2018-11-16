from django import forms
from housename.models import Housename


class UserLoginForms(forms.Form):
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
        model = Housename
        fields = ['house_name']
