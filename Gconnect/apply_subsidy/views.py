from django.shortcuts import render, redirect, get_object_or_404
from . import forms
from .models import ApplySubsidy
from subsidy_priority.models import SubsidyPriority
from django.contrib import messages


def subsidy_application(request):
    login_id = request.session['logid']
    model_object = ApplySubsidy.objects.all()
    prio_obj=SubsidyPriority.objects.all()

    if request.method == 'POST':
        form = forms.ApplySubForms(request.POST, request.FILES)
        #aplctnobj = form.cleaned_data
        #subsidy = aplctnobj['sub_typ']
        #messages.info(request, subsidy)
        #aplctnobj = form.cleaned_data
        #if aplctnobj['sub_typ']!="" and aplctnobj['applicant_name']!="" and aplctnobj['Address_hname']!="" and aplctnobj['Address_po'] and aplctnobj['Address_road']!="" and aplctnobj['mob']!="" and aplctnobj['ward_hno_old']!="" and aplctnobj['ward_hno_new']!="" and aplctnobj['social_cat']!="" and aplctnobj['land_area']!="" and aplctnobj['survey_no']!="" and aplctnobj['prev_subsidy']!="" and aplctnobj['apl_bpl']!="" and aplctnobj['mental_physical_challenge']!="" and  aplctnobj['house_typ']!="" and
        if form.is_valid():
            aplctnobj = form.cleaned_data
            subsidy = aplctnobj['sub_typ']

            applicant = aplctnobj['applicant_name']
            house = aplctnobj['Address_hname']
            po = aplctnobj['Address_po']
            road = aplctnobj['Address_road']
            phn = aplctnobj['mob']
            old_hno = aplctnobj['ward_hno_old']

            new_hno = aplctnobj['ward_hno_new']
            social = aplctnobj['social_cat']
            land = aplctnobj['land_area']
            survey = aplctnobj['survey_no']
            prev_sub = aplctnobj['prev_subsidy']
            apl = aplctnobj['apl_bpl']
            #consideration = aplctnobj['special1_consideration']
            mental_pysical = aplctnobj['mental_physical_challenge']
            type_house = aplctnobj['house_typ']
            ration_no = aplctnobj['ration_card_no']
            adhar = aplctnobj['adhar_card_no']
            id_card = aplctnobj['voter_id']
            elig1 = aplctnobj['first_elig']
            elig2 = aplctnobj['sec_elig']
            elig3 = aplctnobj['third_elig']
            prio1 = aplctnobj['first_prio']
            prio2 = aplctnobj['sec_prio']
            prio3 = aplctnobj['third_prio']
            prio4 = aplctnobj['fourth_prio']
            prio5 = aplctnobj['fifth_prio']
            #con=aplctnobj['spcl_cons']
            #sub_prio_obj = SubsidyPriority.objects.get(subsidy_prio_name=prio1)
            #fsub_prio = sub_prio_obj.subsidy_prio_name
            #fsub_prio_mark1 = sub_prio_obj.subsidy_prio_mark
            #sub_prio_obj2 = SubsidyPriority.objects.get(subsidy_prio_name=prio2)
            #fsub_prio2 = sub_prio_obj2.subsidy_prio_name
            #fsub_prio_mark2 = sub_prio_obj2.subsidy_prio_mark
            #sub_prio_obj3 = SubsidyPriority.objects.get(subsidy_prio_name=prio3)
            #fsub_prio3 = sub_prio_obj3.subsidy_prio_name
            #fsub_prio_mark3= sub_prio_obj3.subsidy_prio_mark
            #sub_prio_obj4 = SubsidyPriority.objects.get(subsidy_prio_name=prio4)
            #fsub_prio4 = sub_prio_obj4.subsidy_prio_name
            #fsub_prio_mark4 = sub_prio_obj4.subsidy_prio_mark
            #sub_prio_obj5 = SubsidyPriority.objects.get(subsidy_prio_name=prio5)
            #fsub_prio5 = sub_prio_obj5.subsidy_prio_name
            #fsub_prio_mark5 = sub_prio_obj5.subsidy_prio_mark
            #total_mark=fsub_prio_mark1+fsub_prio_mark2+fsub_prio_mark3+fsub_prio_mark4+fsub_prio_mark5
            #sta=0
            #l= request.POST.getlist('model_size_ids[]')
            #messages.info(request, str(l))
            #cons = request.POST.get['none']





            # completed = request.POST.get('completed', '') == 'on'
            # if completed=="True":
            #     cons = "widow"
            #     messages.info(request, completed)
            # else:
            #     cons = "not widow"
            #     messages.info(request, completed)
            sta=0
            messages.info(request, login_id)
            application = ApplySubsidy(sub_typ=subsidy, applicant_name=applicant, Address_hname=house, Address_po=po,Address_road=road, mob=phn, ward_hno_old=old_hno, ward_hno_new=new_hno,social_cat=social, land_area=land, survey_no=survey, prev_subsidy=prev_sub, apl_bpl=apl, mental_physical_challenge=mental_pysical, house_typ=type_house, ration_card_no=ration_no, adhar_card_no=adhar, voter_id=id_card, first_elig=elig1, sec_elig=elig2, third_elig=elig3, first_prio=prio1, sec_prio=prio2, third_prio=prio3, fourth_prio=prio4, fifth_prio=prio5,status=sta, login_id=login_id)

            #  special1_consideration=consideration)
            application.save()
            #  msg = "successfully inserted"

            return redirect('apply_subsidy:ApplySubForms')
        else:
            # cons = request.POST.getlist('status')
            # messages.info(request, cons)
            messages.info(request, "form is not valid")
            #messages.info(request, login_id)
    else:
        form = forms.ApplySubForms
    # msg = "not inserted"
    return render(request, "apply_subsidy/apply_subsidy.html", {'form': form, 'data': prio_obj})
