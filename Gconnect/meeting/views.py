from django.shortcuts import render, redirect, get_object_or_404
from . import forms
from .models import Meeting
from django.core.mail import EmailMessage
from housename.models import Housename
from place.models import Place


def meetings(request):
    # login_id = request.session['logid']
    model_object = Meeting.objects.all()


    if request.method == 'POST':
        form = forms.MeetingForms(request.POST, request.FILES)
        if form.is_valid():
            meetingobj = form.cleaned_data
            mplace = meetingobj['place_name']



            mdate = meetingobj['meeting_date']
            mtime = meetingobj['meeting_time']
            agenda = meetingobj['meeting_agenda']
            mid = request.POST.get('place_name')
            model_object_place = Place.objects.get(id=mid)
            #data_place = model_object
            email_body_text = "Hi Meeting details.........    place:"+model_object_place.name+"\n"+"date:"+request.POST.get('meeting_date')+"\n"+"time:"+request.POST.get('meeting_time')+"\n"+"agenda:"+meetingobj["meeting_agenda"]+"\n"
            sp = Meeting(place_name=mplace, meeting_date=mdate, meeting_time=mtime, meeting_agenda=agenda)
            sp.save()
            #str1=' place: '
            #group mail



            for gmails in Housename.objects.all():
                mail_list = gmails.house_mail
                #place = Place.objects.all().filter(name=mplace)[0]
                email = EmailMessage('gramasabha meeting', email_body_text, to=[mail_list])
                email.send()
            return redirect('meeting:MeetingForms')
    else:
        form = forms.MeetingForms

    return render(request, "meeting/meeting.html", {'form': form, 'data': model_object})


def edit_meeting(request, pk):
    template = 'meeting/meeting.html'
    post = get_object_or_404(Meeting, pk=pk)
    model_object = Meeting.objects.all()
    if request.method == 'POST':
        form = forms.MeetingForms(request.POST, instance=post)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect('meeting:MeetingForms')
    else:
        form = forms.MeetingForms(instance=post)
        context = {
            'form': form,
            'post': post,
            'data': model_object,
        }
    return render(request, template, context)


def delete_meeting(request, pk):
    post = get_object_or_404(Meeting, pk=pk)
    post.delete()
    return redirect('meeting:MeetingForms')
