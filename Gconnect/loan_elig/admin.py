from django.contrib import admin
from  .models import LoanEligibility


class LoanEligibilityAdmin(admin.ModelAdmin):
    list_display = ["loan_elig_name"]


admin.site.register(LoanEligibility, LoanEligibilityAdmin)