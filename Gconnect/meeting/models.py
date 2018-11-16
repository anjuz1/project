from django.db import models
from place.models import Place
from datetime import date, time


class Meeting(models.Model):
    place_name = models.ForeignKey(Place, on_delete=models.CASCADE)
    meeting_date = models.DateField(default=date.today)
    meeting_time = models.TimeField()
    meeting_agenda = models.CharField(max_length=200, default='')
    meeting_status = models.IntegerField(default=0)
    meeting_decisions = models.CharField(max_length=500, default='')

    def __str__(self):
        return self.meeting_agenda
