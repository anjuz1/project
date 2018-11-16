from django.db.models import Count
from django.shortcuts import render, redirect
import datetime
from housename.models import Housename
from members.models import Member
from meeting.models import Meeting
from temp_attendance.models import TempAttend
from .models import Gmeeting
from . import forms


def gmeetings(request):
    today = datetime.datetime.today()
    user_val = TempAttend.objects.filter(tm_date=today)
    meeting_obj=Meeting.objects.get(meeting_date=today)
    count = TempAttend.objects.filter(tm_date=today).aggregate(pcount=Count('tm_date'))
    memb_data = Member.objects.all()
    if request.method == 'POST':
        form = forms.GmeetingForms(request.POST, request.FILES)
        if form.is_valid():
            gmobj = form.cleaned_data
            dat = today
            dec = gmobj['decisions']

            user_val = TempAttend.objects.filter(tm_date=today)
            count = TempAttend.objects.filter(tm_date=today).aggregate(pcount=Count('tm_date'))
            # messages.info(request, str(today.date()))
            gm = Gmeeting(decisions=dec, tdate=dat)
            # form_mark_list=total_mark, status=sta, log_id=login_id) special1_consideration=consideration)
            gm.save()
            #  msg = "successfully inserted"
            return redirect('gmeeting:GmeetingForms')
    else:
        form = forms.GmeetingForms

    return render(request, "gmeeting/gmeeting.html",
                  {'form': form, 'data': memb_data, 'datemem': user_val, 'c': count, 'ag': meeting_obj})
