from django.contrib import admin
from .models import ChitDetails


class ChitDetailsAdmin(admin.ModelAdmin):
    list_display = ["chit_name", "members_name", "chit_details_date"]


admin.site.register(ChitDetails, ChitDetailsAdmin)
