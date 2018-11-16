from datetime import date
from meeting.models import Meeting
from members.models import Member
from datetime import date, time
from django.db import models


class Gmeeting(models.Model):

    decisions = models.CharField(max_length=250,default='')
    tdate = models.DateField(default=date.today)

    def __str__(self):
        return self.meeting

