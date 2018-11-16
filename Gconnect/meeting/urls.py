from django.conf.urls import url
from .views import meetings, edit_meeting, delete_meeting

app_name = 'meeting'
urlpatterns = [
    url(r'^$', meetings, name='MeetingForms'),
    url(r'^edit-meeting/(?P<pk>\d+)$', edit_meeting, name='edit_meeting'),
    url(r'^delete-meeting/(?P<pk>\d+)$', delete_meeting, name='delete_meeting'),

]
