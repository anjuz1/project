from django.contrib import admin
from  .models import SubsidyEligibility


class SubsidyEligibilityAdmin(admin.ModelAdmin):
    list_display = ["subsidy_elig_name"]


admin.site.register(SubsidyEligibility, SubsidyEligibilityAdmin)