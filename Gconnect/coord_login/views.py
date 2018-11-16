from django.shortcuts import render, redirect
from .import forms
from coordinator_reg.models import CoordRegistration


def coordhome(request):
    return render(request, 'HomepageCoord/coordhome.html', {'logid': request.session['logid']})


def login(request):
    if request.method == 'POST':
        form = forms.LoginForms(request.POST)
        if form.is_valid():
            userObj = form.cleaned_data
            username = userObj['username']
            password = userObj['password']
            if CoordRegistration.objects.filter(coord_uname=username).exists() and CoordRegistration.objects.filter(coord_pwd=password).exists():
                obj = CoordRegistration.objects.get(coord_uname=username)
                request.session['logid'] = obj.id
                return redirect('coord_login:coordhome')
            else:
                return render(request, 'coord_login/coord_login.html', {'form': form})
    else:
        form = forms.LoginForms()
    return render(request, 'coord_login/coord_login.html', {'form': form})
