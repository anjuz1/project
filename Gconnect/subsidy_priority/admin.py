from django.contrib import admin
from .models import SubsidyPriority


class SubsidyPriorityAdmin(admin.ModelAdmin):
    list_display = ["subsidy_prio_name", "subsidy_prio_mark"]


admin.site.register(SubsidyPriority, SubsidyPriorityAdmin)