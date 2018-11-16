from django.shortcuts import render, redirect, get_object_or_404
from .import forms
from .models import Housename


def user_family_reg(request):
   # login_id = request.session['logid']
    model_object = Housename.objects.all()

    if request.method == 'POST':
        form = forms.HouseNameForms(request.POST, request.FILES)
        if form.is_valid():
            userobj = form.cleaned_data
            name = userobj['house_name']
            num = userobj['house_num']
            po = userobj['house_po']
            place = userobj['house_street']
            district = userobj['house_district']
            state = userobj['house_state']
            adhar = userobj['house_adhar']

            uname = userobj['house_uname']
            pwd = userobj['house_pwd']
            mailid = userobj['house_mail']
            family = Housename(house_name=name, house_num=num, house_po=po, house_street=place, house_district=district, house_state=state, house_adhar=adhar, house_uname=uname, house_pwd=pwd, house_mail=mailid)
            family.save()
          #  msg = "successfully inserted"
            return redirect('housename:HouseNameForms')
    else:
        form = forms.HouseNameForms
       # msg = "not inserted"
    return render(request, "house_name/house_reg.html", {'form': form, 'data': model_object})


def edit_family(request, pk):
    template = 'house_name/house_reg.html'
    post = get_object_or_404(Housename, pk=pk)
    model_object = Housename.objects.all()
    if request.method == 'POST':
        form = forms.HouseNameForms(request.POST, instance=post)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect('housename:HouseNameForms')
    else:
        form = forms.HouseNameForms(instance=post)
        context = {
            'form': form,
            'post': post,
            'data': model_object,
        }
    return render(request, template, context)


def delete_family(request, pk):
    post = get_object_or_404(Housename, pk=pk)
    post.delete()
    return redirect('housename:HouseNameForms')
