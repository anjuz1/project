from datetime import date

from django.db import models
CHOICES = (('male', 'male'), ('female', 'female'), ('others', 'others'))


class WardMembRegistration(models.Model):
    wardmemb_name = models.CharField(max_length=25, default='')
    wardmemb_hname = models.CharField(max_length=25, default='')
    wardmemb_po = models.CharField(max_length=25, default='')
    wardmemb_place = models.CharField(max_length=25, default='')
    wardmemb_phno = models.CharField(max_length=10, default='')
    wardmemb_mailid = models.CharField(max_length=25, default='')
    wardmemb_uname = models.CharField(max_length=25, default='')
    wardmemb_pwd = models.CharField(max_length=25, default='')
    wardmemb_gender = models.CharField(choices=CHOICES, max_length=10)
    wardmemb_dob = models.DateField(default=date.today)

    def __str__(self):
        return self.wardmemb_name
