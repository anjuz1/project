from django.shortcuts import render, redirect
from chit_details.models import ChitDetails
from chit.models import Chit
from .models import ChitFinalInstallment
from members.models import Member
from chit_final_draw.models import ChitFinalDraw
from django.contrib import messages
import datetime


def chitfinalinstallment(request, pk):
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



    if request.method == 'POST':

        today = datetime.datetime.today()
        try:
            fdinstalobj = ChitFinalInstallment.objects.get(fchit_name_id=obj.id, fmember_name_id=mid)
            finstal_date = fdinstalobj.chit_imonth
            if finstal_date.month == today.month:
                messages.info(request, str(memberid.members_name)+'is already completed installment of month:' + today.strftime('%B') + ' is already set!')

            chit_draw_obj = ChitFinalDraw.objects.get(fmember_name_id=memberid.members_name_id)
            if chit_draw_obj.fmember_name_id == memberid.members_name_id:
                messages.info(request, str(memberid.members_name) + ' is the chit draw owner!')
        except ChitFinalDraw.DoesNotExist:
            chit_draw_obj = None

        except ChitFinalInstallment.DoesNotExist:
            fdinstalobj=None
            membcount = ChitDetails.objects.filter(chit_name_id=obj.id).count()
            install_amt = int(amt) / membcount
            c = ChitFinalInstallment(fchit_name_id=obj.id, fmember_name_id=memberid.members_name_id,
                                     chit_install_amount=install_amt, chit_imonth=today)
            c.save()
            #return redirect(request, "chit_memb/memberlist.html")
    return render(request, "chit_final_install/installment.html", {'data': model_object})
