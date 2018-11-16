from django.db import models

from loan_elig.models import LoanEligibility
from loan_priority.models import LoanPriority


class LoanDetails(models.Model):

    loan_elig_name = models.ForeignKey(LoanEligibility, on_delete=models.CASCADE)
    loan_prio_name = models.ForeignKey(LoanPriority, on_delete=models.CASCADE)

    def __str__(self):
        return self.loan_elig_name

