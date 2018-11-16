from django.shortcuts import render, redirect, get_object_or_404
from .import forms
from .models import LoanPriority


def loan_prioritys(request):
   # login_id = request.session['logid']
    model_object = LoanPriority.objects.all()

    if request.method == 'POST':
        form = forms.LoanPrioForms(request.POST, request.FILES)
        if form.is_valid():
            loanprioobj = form.cleaned_data
            loanprioname = loanprioobj['loan_prio_name']
            loanpriomark = loanprioobj['loan_prio_mark']
            sp = LoanPriority(loan_prio_name=loanprioname, loan_prio_mark=loanpriomark)
            sp.save()
            return redirect('loan_priority:LoanPrioForms')
    else:
        form = forms.LoanPrioForms

    return render(request, "loan_priority/loan_prio.html", {'form': form, 'data': model_object})


def edit_loanpriority(request, pk):
    template = 'loan_priority/loan_prio.html'
    post = get_object_or_404(LoanPriority, pk=pk)
    model_object = LoanPriority.objects.all()
    if request.method == 'POST':
        form = forms.LoanPrioForms(request.POST, instance=post)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect('loan_priority:LoanPrioForms')
    else:
        form = forms.LoanPrioForms(instance=post)
        context = {
            'form': form,
            'post': post,
            'data': model_object,
        }
    return render(request, template, context)


def delete_loanpriority(request, pk):
    post = get_object_or_404(LoanPriority, pk=pk)
    post.delete()
    return redirect('loan_priority:LoanPrioForms')
