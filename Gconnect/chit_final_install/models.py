from django.db import models
from chit.models import Chit
from chit_details.models import ChitDetails
from datetime import date, time


class ChitFinalInstallment(models.Model):
    fchit_name = models.ForeignKey(Chit, on_delete=models.CASCADE)
    fmember_name = models.ForeignKey(ChitDetails, on_delete=models.CASCADE)
    chit_install_amount = models.BigIntegerField()
    chit_imonth = models.DateField(default=date.today)

    def __int__(self):
        return self.chit_install_amount
