from datetime import date

from django.db import models
CHOICES = (('male', 'male'), ('female', 'female'), ('others', 'others'))


class CoordRegistration(models.Model):
    coord_name = models.CharField(max_length=45, default='')
    coord_hname = models.CharField(max_length=45, default='')
    coord_po = models.CharField(max_length=45, default='')
    coord_place = models.CharField(max_length=45, default='')
    coord_phno = models.CharField(max_length=10, default='')
    coord_mailid = models.CharField(max_length=50, default='')
    coord_uname = models.CharField(max_length=45, default='')
    coord_pwd = models.CharField(max_length=45, default='')
    coord_gender = models.CharField(choices=CHOICES, max_length=10)
    coord_dob = models.DateField(default=date.today)

    def __str__(self):
        return self.coord_name
