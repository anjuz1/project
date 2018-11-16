from django.shortcuts import render, redirect, get_object_or_404
from .import forms
from .models import SubsidyDetails


def subsidy_details(request):
   # login_id = request.session['logid']
    model_object = SubsidyDetails.objects.all()

    if request.method == 'POST':
        form = forms.SubDetailsForms(request.POST, request.FILES)
        if form.is_valid():
            subdetobj = form.cleaned_data
            subtypname = subdetobj['subsidy_typ_name']
            subeligname = subdetobj['subsidy_elig_name']
            subprioname = subdetobj['subsidy_prio_name']
            sp = SubsidyDetails(subsidy_typ_name=subtypname, subsidy_elig_name=subeligname, subsidy_prio_name=subprioname)
            sp.save()
            return redirect('subsidy_details:SubDetailsForms')
    else:
        form = forms.SubDetailsForms

    return render(request, "sub_details/sub_det.html", {'form': form, 'data': model_object})


def edit_subdetails(request, pk):
    template = 'sub_details/sub_det.html'
    post = get_object_or_404(SubsidyDetails, pk=pk)
    model_object = SubsidyDetails.objects.all()
    if request.method == 'POST':
        form = forms.SubDetailsForms(request.POST, instance=post)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect('subsidy_details:SubDetailsForms')
    else:
        form = forms.SubDetailsForms(instance=post)
        context = {
            'form': form,
            'post': post,
            'data': model_object,
        }
    return render(request, template, context)


def delete_subdetails(request, pk):
    post = get_object_or_404(SubsidyDetails, pk=pk)
    post.delete()
    return redirect('subsidy_details:SubDetailsForms')
