from django.conf.urls import url
from .views import chitdetails, edit_chit_details, delete_chit_details

app_name = 'chit_details'
urlpatterns = [
    url(r'^$', chitdetails, name='ChitDetailsForm'),
    url(r'^edit-chitdetails/(?P<pk>\d+)$', edit_chit_details, name='edit_chit_details'),
    url(r'^delete-chitdetails/(?P<pk>\d+)$', delete_chit_details, name='delete_chit_details'),

]