from django.shortcuts import render, redirect, get_object_or_404
from .import forms
from .models import Chit


def chits(request):
    login_id = request.session['logid']
    model_object = Chit.objects.filter(login_id=login_id)
    if request.method == 'POST':
        form = forms.ChitForms(request.POST, request.FILES)
        if form.is_valid():
            chitobj=form.cleaned_data
            chit_name=chitobj['chit_name']
            amount = chitobj['chit_amount']
            start_date = chitobj['chit_start_date']
            c = Chit(chit_amount=amount, chit_start_date=start_date, chit_name=chit_name, login_id=login_id)
            c.save()
            return redirect('chit:ChitForms')
    else:
        form = forms.ChitForms

    return render(request, "chit/chit.html", {'form': form, 'data': model_object})


def edit_chit(request, pk):
    template = 'places/place.html'
    post = get_object_or_404(Chit, pk=pk)
    model_object = Chit.objects.all()
    if request.method == 'POST':
        form = forms.ChitForms(request.POST, instance=post)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect('chit:ChitForms')
    else:
        form = forms.ChitForms(instance=post)
        context = {
            'form': form,
            'post': post,
            'data': model_object,
        }
    return render(request, template, context)


def delete_chit(request, pk):
    post = get_object_or_404(Chit, pk=pk)
    post.delete()
    return redirect('chit:ChitForms')
