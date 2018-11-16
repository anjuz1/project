from django.db import models
from subsidy_types.models import SubsidyTypes
from subsidy_elig.models import SubsidyEligibility


class SubsidyPriority(models.Model):
    #subsidy_ptype = models.ForeignKey(SubsidyTypes, on_delete=models.CASCADE)
    #subsidy_pelig = models.ForeignKey(SubsidyEligibility, on_delete=models.CASCADE)
    subsidy_prio_name = models.CharField(max_length=50, default='')
    subsidy_prio_mark = models.BigIntegerField()

    def __str__(self):
        return self.subsidy_prio_name

