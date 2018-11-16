from django.shortcuts import render, redirect
from .import forms
from housename.models import Housename


def userhome(request):
    return render(request, 'HomepageUser/userhome.html', {'logid': request.session['logid']})


def login(request):
    if request.method == 'POST':
        form = forms.UserLoginForms(request.POST)
        if form.is_valid():
            userObj = form.cleaned_data
            username = userObj['username']
            password = userObj['password']
            if Housename.objects.filter(house_uname=username).exists() and Housename.objects.filter(house_pwd=password).exists():
                obj = Housename.objects.get(house_uname=username)
                request.session['logid'] = obj.id
                return redirect('user_login:userhome')
            else:
                return render(request, 'user_login/user_login.html', {'form': form})
    else:
        form = forms.UserLoginForms()
    return render(request, 'user_login/user_login.html', {'form': form})
