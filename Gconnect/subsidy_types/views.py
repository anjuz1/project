from django.shortcuts import render, redirect, get_object_or_404
from .import forms
from .models import SubsidyTypes


def subsidy_types(request):
   # login_id = request.session['logid']
    model_object = SubsidyTypes.objects.all()

    if request.method == 'POST':
        form = forms.SubTypeForms(request.POST, request.FILES)
        if form.is_valid():
            subtypeobj = form.cleaned_data
            subtypename = subtypeobj['subsidy_type_name']
            subtypesub = subtypeobj['subsidy_type_sub_perc']
            subtypeself = subtypeobj['subsidy_type_self_perc']
            sp = SubsidyTypes(subsidy_type_name=subtypename, subsidy_type_sub_perc=subtypesub, subsidy_type_self_perc=subtypeself)
            sp.save()
            return redirect('subsidy_types:SubTypeForms')
    else:
        form = forms.SubTypeForms

    return render(request, "subsidy_types/sub_types.html", {'form': form, 'data': model_object})


def edit_subtypes(request, pk):
    template = 'subsidy_types/sub_types.html'
    post = get_object_or_404(SubsidyTypes, pk=pk)
    model_object = SubsidyTypes.objects.all()
    if request.method == 'POST':
        form = forms.SubTypeForms(request.POST, instance=post)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect('subsidy_types:SubTypeForms')
    else:
        form = forms.SubTypeForms(instance=post)
        context = {
            'form': form,
            'post': post,
            'data': model_object,
        }
    return render(request, template, context)


def delete_subtypes(request, pk):
    post = get_object_or_404(SubsidyTypes, pk=pk)
    post.delete()
    return redirect('subsidy_types:SubTypeForms')
