from django.shortcuts import render, redirect
from chit_details.models import ChitDetails
from chit.models import Chit
from .models import ChitFinalDraw
from members.models import Member
import datetime
from django.contrib import messages


def chitfinaldraw(request, pk):
    model_object = ChitDetails.objects.filter(id=pk)

    memberid = ChitDetails.objects.get(id=pk)
    amountmodel=Chit.objects.filter()
    obj = Chit.objects.get(id=request.session['amount'])
    chitname = obj.chit_name

    amt = obj.chit_amount
    #model_object_m = ChitDetails.objects.filter(chit_name_id=obj.id)
    mid = memberid.members_name_id
    obj_memb = Member.objects.get(id=mid)
    #membname = obj_memb.member_name
    #model_object_draw = ChitFinalDraw.objects.get(fchit_name_id=obj.id, fmember_name_id=memberid.members_name_id)

    #print(obj_memb.member_name)
    if request.method == 'POST':
        #chname=amountmodel.chit_name
        #mename=model_object.members_name
        #print()
        today = datetime.datetime.today()
        try:
            fdrawobj = ChitFinalDraw.objects.get(fchit_name_id=obj.id)
            fdraw_date = fdrawobj.chit_month
            if fdraw_date.month == today.month:
                messages.info(request,'month:'+today.strftime('%B') + ' is already set!')
        except ChitFinalDraw.DoesNotExist:
            fdrawobj=None
            c = ChitFinalDraw(fchit_name_id=obj.id, fmember_name_id=obj_memb.id, chit_install_amount=amt, chit_month=today)
            c.save()

    #model_object_draw = ChitFinalDraw.objects.filter(fchit_name_id=obj.id, fmember_name_id=memberid.members_name_id)
    return render(request, "chit_final_draw/draw.html", {'data': model_object})
