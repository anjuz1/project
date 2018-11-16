from django.contrib import admin
from .models import Chit


class ChitAdmin(admin.ModelAdmin):
    list_display = ["chit_amount", "chit_start_date", "chit_name"]


admin.site.register(Chit, ChitAdmin)


