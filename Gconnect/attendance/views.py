from django.shortcuts import render, redirect
from . import forms
from temp_attendance.models import TempAttend
import datetime
from housename.models import Housename
from members.models import Member
from meeting.models import Meeting
from django.contrib import messages


def attendance(request):

    memb_data = Member.objects.all()
    today = datetime.datetime.today()
    form = forms.AttendanceForms(request.POST, request.FILES)
    size=TempAttend.objects.filter(tm_date=today).count()
    return render(request, "attendance/attendance.html",
                  {'form': form, 'data': memb_data, 'count': size,'datest': today})



def memb_attendance(request, pk):
    today = datetime.datetime.today()
    memb_data = Member.objects.all()

    form = forms.AttendanceForms(request.POST, request.FILES)
    user_val = TempAttend.objects.filter(t_member=pk, tm_date=today)
    #messages.info(request, str(today.date()))
    user_date = TempAttend.objects.filter(tm_date=today)
    user = TempAttend.objects.all()

    if user_val.exists():
        s="present"
        return render(request, "attendance/attendance.html",
                      {'form': form, 'data': memb_data, 'status': s, 'datest': today,'mem':user,'datemem':user_date})
    else:
        a = TempAttend(t_member=pk, tm_date=today,status="present")
        a.save()
        s = "present"
        return render(request, "attendance/attendance.html",
                      {'form': form, 'data': memb_data, 'status': s, 'datest': today,'mem':user,'datemem':user_date})






#   memb_data = Member.objects.all()
#  if request.method == 'POST':
#     form = forms.AttendanceForms(request.POST, request.FILES)
#    if form.is_valid():
#       attendenceobj=form.cleaned_data
#      meeting_ag=attendenceobj['meeting']
#     date=attendenceobj['m_date']
#    members=model_object_m.id
#   a = Attendances(meeting=meeting_ag, m_date=date, member=members)
#  a.save()

    return render(request, "attendance/attendance.html", {'form': form, 'data': memb_data})
