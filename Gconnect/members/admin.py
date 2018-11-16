from django.contrib import admin
from .models import Member


class MemberAdmin(admin.ModelAdmin):
    list_display = ["member_name", "member_age", "member_education", "member_job", "member_phnum", "member_mailid", "member_gender", "member_social_cat", "member_consideration","house_name"]


admin.site.register(Member, MemberAdmin)
