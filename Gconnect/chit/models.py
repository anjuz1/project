from datetime import date

from django.db import models


class Chit(models.Model):
    chit_amount = models.CharField(max_length=10, default='')
    chit_start_date = models.DateField(default=date.today)
    chit_name = models.CharField(max_length=20, default='')
    login_id = models.BigIntegerField()

    def __str__(self):
        return self.chit_name

