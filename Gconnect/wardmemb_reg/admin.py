from django.contrib import admin
from .models import WardMembRegistration


class WardMembAdmin(admin.ModelAdmin):
    list_display = ["wardmemb_name", "wardmemb_hname", "wardmemb_po", "wardmemb_place", "wardmemb_gender", "wardmemb_dob", "wardmemb_phno", "wardmemb_mailid", "wardmemb_uname", "wardmemb_pwd"]


admin.site.register(WardMembRegistration, WardMembAdmin)
