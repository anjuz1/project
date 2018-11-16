from django.shortcuts import render, redirect
from .import forms


def wardmemb_reg(request):
    if request.method == "POST":
        form = forms.WardMembRegForms(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            msg = "Inserted Successfully"
            return redirect('wardmemb_reg:WardMembRegForms')
    else:
        form = forms.WardMembRegForms
        msg = "not inserted"
    return render(request, "wardmemb_reg/wardmemb_reg.html", {'form': form, 'msg': msg})

