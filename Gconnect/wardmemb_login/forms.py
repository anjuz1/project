from django import forms
# from Centers.models import Centers


class Login_Ward_Forms(forms.Form):
    username = forms.CharField(required=True, label='Username', max_length=30)
    password = forms.CharField(required=True, label='Password', max_length=30, widget=forms.PasswordInput())

