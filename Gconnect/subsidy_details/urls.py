from django.conf.urls import url
from .views import subsidy_details, delete_subdetails, edit_subdetails

app_name = 'subsidy_details'
urlpatterns = [
    url(r'^$', subsidy_details, name='SubDetailsForms'),
    url(r'^edit-subdetail/(?P<pk>\d+)$', edit_subdetails, name='edit_subdetails'),
    url(r'^delete-subdetail(?P<pk>\d+)$', delete_subdetails, name='delete_subdetails'),

]
