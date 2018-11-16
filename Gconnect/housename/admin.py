from django.contrib import admin
from .models import Housename


class HouseAdmin(admin.ModelAdmin):
    list_display = ["house_name", "house_num", "house_po", "house_street", "house_district", "house_state", "house_adhar", "house_uname", "house_pwd", "house_mail"]


admin.site.register(Housename, HouseAdmin)
