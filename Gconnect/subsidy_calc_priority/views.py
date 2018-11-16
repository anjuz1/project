from django.shortcuts import render


from subsidy_priority.models import  SubsidyPriority
from apply_subsidy.models import ApplySubsidy
from django.contrib import messages


def calc_priority(request,pk):
    subsidy_obj=ApplySubsidy.objects.get(id=pk)
    subsidyprio_obj=SubsidyPriority.objects.all()

    tot=0

    #messages.info(request, subsidyprio_obj.subsidy_prio_name)
    for prios in subsidyprio_obj:

        p1 = SubsidyPriority.objects.get(id=subsidy_obj.first_prio_id)
        #or subsidy_obj.sec_prio_id or subsidy_obj.third_prio_id or subsidy_obj.fourth_prio or subsidy_obj.fifth_prio)
        p2=SubsidyPriority.objects.get(id=subsidy_obj.sec_prio_id)
        p3 = SubsidyPriority.objects.get(id=subsidy_obj.third_prio_id)
        p4 = SubsidyPriority.objects.get(id=subsidy_obj.fourth_prio_id)
        p5 = SubsidyPriority.objects.get(id=subsidy_obj.fifth_prio_id)
        tot=p1.subsidy_prio_mark+p2.subsidy_prio_mark+p3.subsidy_prio_mark+p4.subsidy_prio_mark+p5.subsidy_prio_mark
        t = ApplySubsidy.objects.get(id=pk)
        t.status = 1  # change field
        t.save()  # this will update only
        sta=t.status
        #messages.info(request,"total="+str(p1.subsidy_prio_name))
        #messages.info(request, tot)
        return render(request, "subsidy_approve/approve.html", {'obj': subsidy_obj, 'data': subsidyprio_obj, 'p1': p1,'p2': p2,'p3': p3,'p4': p4,'p5': p5, 'tot': tot})



    return render(request, "subsidy_approve/approve.html", {'obj': subsidy_obj, 'data':subsidyprio_obj})


