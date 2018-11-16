from django.db import models


class SubsidyTypes(models.Model):
    subsidy_type_name = models.CharField(max_length=50, default='')
    subsidy_type_sub_perc = models.IntegerField()
    subsidy_type_self_perc = models.IntegerField()

    def __str__(self):
        return self.subsidy_type_name