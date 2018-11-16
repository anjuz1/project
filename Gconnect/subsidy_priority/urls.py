from django.conf.urls import url
from .views import subsidy_prioritys, delete_subpriority, edit_subpriority

app_name = 'subsidy_priority'
urlpatterns = [
    url(r'^$', subsidy_prioritys, name='SubPrioForms'),
    url(r'^edit-subpriority/(?P<pk>\d+)$', edit_subpriority, name='edit_subpriority'),
    url(r'^delete-subpriority/(?P<pk>\d+)$', delete_subpriority, name='delete_subpriority'),

]
