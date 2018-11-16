from django.shortcuts import render, redirect, get_object_or_404
from .import forms
from .models import LoanEligibility


def loanelig(request):
    model_object = LoanEligibility.objects.all()

    if request.method == 'POST':
        form = forms.LoanEligForms(request.POST, request.FILES)
        if form.is_valid():
            loanprioobj = form.cleaned_data
            loaneligname = loanprioobj['loan_elig_name']

            sp = LoanEligibility(loan_elig_name=loaneligname)
            sp.save()
            return redirect('loan_elig:LoanEligForms')
    else:
        form = forms.LoanEligForms

    return render(request, "loan_elig/loan_elig.html", {'form': form, 'data': model_object})


def edit_loaneligibility(request, pk):
    template = 'loan_elig/loan_elig.html'
    post = get_object_or_404(LoanEligibility, pk=pk)
    model_object = LoanEligibility.objects.all()
    if request.method == 'POST':
        form = forms.LoanEligForms(request.POST, instance=post)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect('loan_elig:LoanEligForms')
    else:
        form = forms.LoanEligForms(instance=post)
        context = {
            'form': form,
            'post': post,
            'data': model_object,
        }
    return render(request, template, context)


def delete_loaneligibility(request, pk):
    post = get_object_or_404(LoanEligibility, pk=pk)
    post.delete()
    return redirect('loan_elig:LoanEligForms')
