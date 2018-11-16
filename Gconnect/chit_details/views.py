from django.shortcuts import render, redirect, get_object_or_404
from . models import ChitDetails
from .import forms


def chitdetails(request):
    model_object = ChitDetails.objects.all()
    if request.method == "POST":
        form = forms.ChitDetailsForm(request.POST, request.FILES)
        if form.is_valid():
            chitdetailsobj = form.cleaned_data
            instance = form.save(commit=False)
            instance.save()
            #msg = "Inserted Successfully"
            return redirect('chit_details:ChitDetailsForm')
    else:
        form = forms.ChitDetailsForm
        #msg = "not inserted"
    return render(request, "chit_details/chit_details.html", {'form': form, 'data': model_object})


def edit_chit_details(request, pk):
    template = 'chit_details/chit_details.html'
    post = get_object_or_404(ChitDetails, pk=pk)
    model_object = ChitDetails.objects.all()
    if request.method == 'POST':
        form = forms.ChitDetailsForm(request.POST, instance=post)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect('chit_details:ChitDetailsForm')
    else:
        form = forms.ChitDetailsForm(instance=post)
        context = {
            'form': form,
            'post': post,
            'data': model_object,
        }
    return render(request, template, context)


def delete_chit_details(request, pk):
    post = get_object_or_404(ChitDetails, pk=pk)
    post.delete()
    return redirect('chit_details:ChitDetailsForm')
