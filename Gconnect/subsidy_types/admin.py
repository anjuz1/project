from django.contrib import admin
from .models import SubsidyTypes


class SubsidyTypeAdmin(admin.ModelAdmin):
    list_display = ["subsidy_type_name", "subsidy_type_sub_perc", "subsidy_type_self_perc"]


admin.site.register(SubsidyTypes,SubsidyTypeAdmin)