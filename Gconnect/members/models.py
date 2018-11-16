from django.db import models
from housename.models import Housename
CHOICES = (('male', 'male'), ('female', 'female'), ('others', 'others'))


class Member(models.Model):
    member_name = models.CharField(max_length=25, default='')
    member_age = models.IntegerField()
    member_education = models.CharField(max_length=25, default='')
    member_job =models.CharField(max_length=25, default='')
    member_phnum = models.CharField(max_length=10, default='')
    member_mailid = models.CharField(max_length=50, default='')
    member_gender = models.CharField(choices=CHOICES, max_length=10)
    member_social_cat = models.CharField(max_length=25, default='')
    member_consideration = models.CharField(max_length=25, default='')
    house_name = models.ForeignKey(Housename, on_delete=models.CASCADE)

    def __str__(self):
        return self.member_name
