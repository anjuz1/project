from django.shortcuts import render, redirect, get_object_or_404
from .import forms
from .models import CoordRegistration
from django.core.mail import EmailMessage
from django.contrib import messages
from . import models


def coord_reg(request):
   # login_id = request.session['logid']
    model_object = CoordRegistration.objects.all()

    if request.method == 'POST':
        form = forms.CoordRegForms(request.POST, request.FILES)
        if form.is_valid():
            coordregobj = form.cleaned_data
            name = coordregobj['coord_name']
            hname = coordregobj['coord_hname']
            po = coordregobj['coord_po']
            place = coordregobj['coord_place']
            phno = coordregobj['coord_phno']
            mailid = coordregobj['coord_mailid']
            uname = coordregobj['coord_uname']
            pwd = coordregobj['coord_pwd']
            gender = coordregobj['coord_gender']
            dob = coordregobj['coord_dob']
            cpwd = coordregobj['confirm_pwd']
            minlen = 8
            user_val = models.CoordRegistration.objects.filter(coord_uname=uname)
            if user_val.exists():
                messages.info(request, 'username already exists!')
            elif len(pwd) < minlen:
                messages.info(request, 'password should be atleast 8 characters!')
            elif pwd == cpwd:
                messages.info(request, 'you inserted successfully')

                coord = CoordRegistration(coord_name=name, coord_hname=hname, coord_po=po, coord_place=place, coord_phno=phno, coord_mailid=mailid, coord_uname=uname, coord_pwd=pwd, coord_gender=gender, coord_dob=dob)
                coord.save()
                email = EmailMessage('gramasabha coordinator registration', 'Congratulations!Successfully registered.    username:  '+uname+'          password:   '+pwd, to=[mailid])
                email.send()

                return redirect('coordinator_reg:CoordRegForms')
            else:
                messages.info(request, 'password mismatch')
                form = forms.CoordRegForms
                #return redirect('coordinator_reg:CoordRegForms')
            return render(request, "coord_reg/coordinator_reg.html", {'form': form})
    else:
        form = forms.CoordRegForms
        msg = "not inserted"
    return render(request, "coord_reg/coordinator_reg.html", {'form': form, 'msg': msg, 'data': model_object})


def edit_coordreg(request, pk):
    template = 'coord_reg/coordinator_reg.html'
    post = get_object_or_404(CoordRegistration, pk=pk)
    model_object = CoordRegistration.objects.all()
    if request.method == 'POST':
        form = forms.CoordRegForms(request.POST, instance=post)
        if form.is_valid():
            coordregobj = form.cleaned_data
            uname = coordregobj['coord_uname']
            pwd = coordregobj['coord_pwd']

            mailid = coordregobj['coord_mailid']
            instance = form.save(commit=False)
            instance.save()
            email = EmailMessage('gramasabha coordinator registration',
                                 'Congratulations!Successfully registered.    username:  ' + uname + '          password:   ' + pwd,
                                 to=[mailid])
            email.send()
            return redirect('coordinator_reg:CoordRegForms')
    else:
        form = forms.CoordRegForms(instance=post)
        context = {
            'form': form,
            'post': post,
            'data': model_object,
        }
    return render(request, template, context)


def delete_coordreg(request, pk):
    post = get_object_or_404(CoordRegistration, pk=pk)
    post.delete()
    return redirect('coordinator_reg:CoordRegForms')
