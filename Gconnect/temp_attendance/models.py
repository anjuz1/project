from datetime import date

from datetime import date, time
from django.db import models


class TempAttend(models.Model):
    t_member = models.BigIntegerField()
    tm_date = models.DateField(default=date.today)
    status = models.CharField(max_length=10, default='')

    def __str__(self):
        return self.tm_date

