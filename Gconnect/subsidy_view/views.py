from django.shortcuts import render

from apply_subsidy.models import ApplySubsidy

def ViewSubsidy(request):
    subsidy_obj=ApplySubsidy.objects.all()




    return render(request, "view_subsidy/view_sub.html", {'data': subsidy_obj})

