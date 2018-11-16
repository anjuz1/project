from django.shortcuts import render, redirect
#from . import forms
#from . models import ChitInstallment
from chit.models import Chit


def chitdraw(request):
    model_object = Chit.objects.all()
    #req=request.session['id']
    #request.session['id']=model_object.id

    #if request.method =='POST':
        #form =
    return render(request, "chit_draw/chit_draw.html", {'data': model_object})

