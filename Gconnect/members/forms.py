from django import forms
from .import models


class MemberForms(forms.ModelForm):
    class Meta:
        model = models.Member
        fields = ['member_name', 'member_age', 'member_education', 'member_job', 'member_phnum', 'member_mailid', 'member_gender', 'member_social_cat', 'member_consideration', 'house_name']
