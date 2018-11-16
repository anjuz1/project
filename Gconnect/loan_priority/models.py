from django.db import models


class LoanPriority(models.Model):
    loan_prio_name = models.CharField(max_length=50, default='')
    loan_prio_mark = models.IntegerField()

    def __str__(self):
        return self.loan_prio_name

