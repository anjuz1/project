from django.db import models


class LoanEligibility(models.Model):
    loan_elig_name = models.CharField(max_length=50, default='')

    def __str__(self):
        return self.loan_elig_name
