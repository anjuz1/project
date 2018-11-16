from django.db import models
from subsidy_types.models import SubsidyTypes
from subsidy_elig.models import SubsidyEligibility
from subsidy_priority.models import SubsidyPriority


class SubsidyDetails(models.Model):
    subsidy_typ_name = models.ForeignKey(SubsidyTypes, on_delete=models.CASCADE)
    subsidy_elig_name = models.ForeignKey(SubsidyEligibility, on_delete=models.CASCADE)
    subsidy_prio_name = models.ForeignKey(SubsidyPriority, on_delete=models.CASCADE)

    def __str__(self):
        return self.subsidy_typ_name

