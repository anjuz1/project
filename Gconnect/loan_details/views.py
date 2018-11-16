from django.shortcuts import render, redirect, get_object_or_404
from .import forms
from .models import LoanDetails


def loan_details(request):
   # login_id = request.session['logid']
    model_object = LoanDetails.objects.all()

    if request.method == 'POST':
        form = forms.LoanDetailsForms(request.POST, request.FILES)
        if form.is_valid():
            loandetobj = form.cleaned_data
            loantypname = loandetobj['loan_elig_name']
            loaneligname = loandetobj['loan_prio_name']

            sp = LoanDetails(loan_elig_name=loantypname, loan_prio_name=loaneligname)
            sp.save()
            return redirect('loan_details:LoanDetailsForms')
    else:
        form = forms.LoanDetailsForms

    return render(request, "loan_details/loan_det.html", {'form': form, 'data': model_object})


def edit_loandetails(request, pk):
    template = 'loan_details/loan_det.html'
    post = get_object_or_404(LoanDetails, pk=pk)
    model_object = LoanDetails.objects.all()
    if request.method == 'POST':
        form = forms.LoanDetailsForms(request.POST, instance=post)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect('loan_details:LoanDetailsForms')
    else:
        form = forms.LoanDetailsForms(instance=post)
        context = {
            'form': form,
            'post': post,
            'data': model_object,
        }
    return render(request, template, context)


def delete_loandetails(request, pk):
    post = get_object_or_404(LoanDetails, pk=pk)
    post.delete()
    return redirect('loan_details:LoanDetailsForms')
