from django.shortcuts import render, redirect, get_object_or_404
from .import forms
from .models import SubsidyEligibility


def subelig(request):
    model_object = SubsidyEligibility.objects.all()

    if request.method == 'POST':
        form = forms.SubEligForms(request.POST, request.FILES)
        if form.is_valid():
            subprioobj = form.cleaned_data
            subeligname = subprioobj['subsidy_elig_name']
            subsidytype = subprioobj['subsidy_ftype']
            #subpriomark = subprioobj['subsidy_prio_mark']
            sp = SubsidyEligibility(subsidy_elig_name=subeligname, subsidy_ftype=subsidytype)
            sp.save()
            return redirect('subsidy_elig:SubEligForms')
    else:
        form = forms.SubEligForms

    return render(request, "subsidy_elig/sub_elig.html", {'form': form, 'data': model_object})


def edit_subeligibility(request, pk):
    template = 'subsidy_elig/sub_elig.html'
    post = get_object_or_404(SubsidyEligibility, pk=pk)
    model_object = SubsidyEligibility.objects.all()
    if request.method == 'POST':
        form = forms.SubEligForms(request.POST, instance=post)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect('subsidy_elig:SubEligForms')
    else:
        form = forms.SubEligForms(instance=post)
        context = {
            'form': form,
            'post': post,
            'data': model_object,
        }
    return render(request, template, context)


def delete_subeligibility(request, pk):
    post = get_object_or_404(SubsidyEligibility, pk=pk)
    post.delete()
    return redirect('subsidy_elig:SubEligForms')
