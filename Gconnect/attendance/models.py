from datetime import date
from meeting.models import Meeting
from members.models import Member
from datetime import date, time
from django.db import models


class Attendances(models.Model):
    meeting = models.ForeignKey(Meeting, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    m_date = models.DateField(default=date.today)

    def __str__(self):
        return self.meeting

