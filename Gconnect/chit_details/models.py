from django.db import models
from datetime import date
from chit.models import Chit
from members.models import Member


class ChitDetails(models.Model):
    chit_name = models.ForeignKey(Chit, on_delete=models.CASCADE)
    members_name = models.ForeignKey(Member, on_delete=models.CASCADE)
    chit_details_date = models.DateField(default=date.today)

    def __str__(self):
        return self.members_name
