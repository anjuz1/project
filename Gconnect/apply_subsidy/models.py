from datetime import date
from django.db import models
from subsidy_types.models import SubsidyTypes
from members.models import Member
from  housename.models import Housename
from subsidy_elig.models import SubsidyEligibility
from  subsidy_priority.models import SubsidyPriority


class ApplySubsidy(models.Model):
    sub_typ = models.ForeignKey(SubsidyTypes, on_delete=models.CASCADE)
    applicant_name = models.ForeignKey(Member, on_delete=models.CASCADE)
    Address_hname = models.ForeignKey(Housename, on_delete=models.CASCADE)
    Address_po = models.CharField(max_length=20, default='')
    Address_road = models.CharField(max_length=20, default='')
    mob= models.CharField(max_length=10, default='')
    ward_hno_old = models.BigIntegerField()
    ward_hno_new = models.BigIntegerField()
    social_cat = models.CharField(max_length=20, default='')
    land_area = models.CharField(max_length=20, default='')
    survey_no = models.CharField(max_length=20, default='')
    prev_subsidy = models.CharField(max_length=20, default='')
    apl_bpl = models.CharField(max_length=10, default='')
    #special1_consideration = models.CharField(max_length=20, default='')
    mental_physical_challenge = models.CharField(max_length=10, default='')
    house_typ = models.CharField(max_length=20, default='')
    ration_card_no = models.CharField(max_length=20, default='')
    adhar_card_no = models.CharField(max_length=20, default='')
    voter_id = models.CharField(max_length=20, default='')
    first_elig = models.ForeignKey(SubsidyEligibility, on_delete=models.CASCADE, default=8)
    sec_elig = models.ForeignKey(SubsidyEligibility, on_delete=models.CASCADE,  related_name='elig_sec',default=8)
    third_elig = models.ForeignKey(SubsidyEligibility, on_delete=models.CASCADE, related_name='elig_third', default=8)
    first_prio = models.ForeignKey(SubsidyPriority, on_delete=models.CASCADE,default=15)
    sec_prio = models.ForeignKey(SubsidyPriority, on_delete=models.CASCADE,related_name='prio_sec',default=15)
    third_prio = models.ForeignKey(SubsidyPriority, on_delete=models.CASCADE,related_name='prio_third',default=15)
    fourth_prio = models.ForeignKey(SubsidyPriority, on_delete=models.CASCADE,related_name='prio_fourth',default=15)
    fifth_prio = models.ForeignKey(SubsidyPriority, on_delete=models.CASCADE,related_name='prio_fifth',default=15)
    #spcl_cons = models.CharField(max_length=100, default='')
    #spcl_cons = models.ManyToManyField(Choices)
    #form_mark_list = models.BigIntegerField()
    status=models.BigIntegerField()
    login_id = models.BigIntegerField()

    def __str__(self):
        return self.sub_typ

