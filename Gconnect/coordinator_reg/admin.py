from django.contrib import admin
from .models import CoordRegistration


class CoordRegAdmin(admin.ModelAdmin):
    list_display = ["coord_name", "coord_hname", "coord_po", "coord_place", "coord_gender", "coord_dob", "coord_phno", "coord_mailid", "coord_uname", "coord_pwd"]


admin.site.register(CoordRegistration, CoordRegAdmin)
