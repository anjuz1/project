from django.contrib import admin
from .models import Meeting


class MeetingAdmin(admin.ModelAdmin):
    list_display = ["place_name", "meeting_date", "meeting_time", "meeting_agenda", "meeting_status", "meeting_decisions"]


admin.site.register(Meeting, MeetingAdmin)