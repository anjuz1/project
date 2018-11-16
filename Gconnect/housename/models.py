from django.db import models


class Housename(models.Model):
    house_name = models.CharField(max_length=45, default='')
    house_num = models.CharField(max_length=25, default='')
    house_po = models.CharField(max_length=50, default='')
    house_street = models.CharField(max_length=50, default='')
    house_district = models.CharField(max_length=50, default='Ernakulam')

    house_state = models.CharField(max_length=25, default='Kerala')
    house_adhar = models.CharField(max_length=38, default='')

    house_uname = models.CharField(max_length=15, default='')
    house_pwd = models.CharField(max_length=15, default='')
    house_mail = models.CharField(max_length=50, default='')

    def __str__(self):
        return self.house_name