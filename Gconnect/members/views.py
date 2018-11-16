from django.shortcuts import render, redirect, get_object_or_404
from .import forms
#from .models import Meeting
#from django.core.mail import EmailMessage
from .models import Member

def members(request):
   # login_id = request.session['logid']
    #model_object = Meeting.objects.all()
    model_object = Member.objects.all()
    if request.method == 'POST':
        form = forms.MemberForms(request.POST, request.FILES)
        if form.is_valid():
            memberobj = form.cleaned_data
            name = memberobj['member_name']
            age = memberobj['member_age']
            edu = memberobj['member_education']
            job = memberobj['member_job']
            phn = memberobj['member_phnum']
            mail = memberobj['member_mailid']
            gend = memberobj['member_gender']
            soc_cat = memberobj['member_social_cat']
            consid = memberobj['member_consideration']
            house = memberobj['house_name']
            sp = Member(member_name=name, member_age=age, member_education=edu, member_job=job, member_phnum=phn, member_mailid=mail, member_gender=gend, member_social_cat=soc_cat, member_consideration=consid, house_name=house)
            sp.save()
            #list_mail = [model_object_member.member_mailid]
            #email = EmailMessage('gramasabha meeting','Place    :     '+place+'     date:    '+mdate+'      time:  '+mtime+'      agenda: '+agenda, to=[list_mail])
            #email.send()
            return redirect('members:MemberForms')
    else:
        form = forms.MemberForms

    return render(request, "member/memb.html", {'form': form, 'data': model_object})


def edit_member(request, pk):
    template = 'member/memb.html'
    post = get_object_or_404(Member, pk=pk)
    model_object = Member.objects.all()
    if request.method == 'POST':
        form = forms.MemberForms(request.POST, instance=post)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect('members:MemberForms')
    else:
        form = forms.MemberForms(instance=post)
        context = {
            'form': form,
            'post': post,
            'data': model_object,
        }
    return render(request, template, context)


def delete_member(request, pk):
    post = get_object_or_404(Member, pk=pk)
    post.delete()
    return redirect('members:MemberForms')
