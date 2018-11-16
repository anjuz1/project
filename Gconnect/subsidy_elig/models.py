from django.db import models
from subsidy_types.models import SubsidyTypes


class SubsidyEligibility(models.Model):
    subsidy_ftype = models.ForeignKey(SubsidyTypes, on_delete=models.CASCADE)
    subsidy_elig_name = models.CharField(max_length=50, default='')

    def __str__(self):
        return self.subsidy_elig_name
