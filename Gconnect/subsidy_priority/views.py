from django.shortcuts import render, redirect, get_object_or_404
from .import forms
from .models import SubsidyPriority


def subsidy_prioritys(request):
   # login_id = request.session['logid']
    model_object = SubsidyPriority.objects.all()

    if request.method == 'POST':
        form = forms.SubPrioForms(request.POST, request.FILES)
        if form.is_valid():
            subprioobj = form.cleaned_data
            #subtype = subprioobj['subsidy_ptype']
            #subelig= subprioobj['subsidy_pelig']
            subprioname = subprioobj['subsidy_prio_name']
            subpriomark = subprioobj['subsidy_prio_mark']
            sp = SubsidyPriority(subsidy_prio_name=subprioname, subsidy_prio_mark=subpriomark)
            #'subsidy_ptype', 'subsidy_pelig',
            sp.save()
            return redirect('subsidy_priority:SubPrioForms')
    else:
        form = forms.SubPrioForms

    return render(request, "sub_priority/sub_prio.html", {'form': form, 'data': model_object})


def edit_subpriority(request, pk):
    template = 'sub_priority/sub_prio.html'
    post = get_object_or_404(SubsidyPriority, pk=pk)
    model_object = SubsidyPriority.objects.all()
    if request.method == 'POST':
        form = forms.SubPrioForms(request.POST, instance=post)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect('subsidy_priority:SubPrioForms')
    else:
        form = forms.SubPrioForms(instance=post)
        context = {
            'form': form,
            'post': post,
            'data': model_object,
        }
    return render(request, template, context)


def delete_subpriority(request, pk):
    post = get_object_or_404(SubsidyPriority, pk=pk)
    post.delete()
    return redirect('subsidy_priority:SubPrioForms')
