from django import forms
from . import models


class WardMembRegForms(forms.ModelForm):
    class Meta:
        model = models.WardMembRegistration
        fields = ['wardmemb_name', 'wardmemb_hname', 'wardmemb_po', 'wardmemb_place', 'wardmemb_gender', 'wardmemb_dob', 'wardmemb_phno', 'wardmemb_mailid', 'wardmemb_uname', 'wardmemb_pwd']