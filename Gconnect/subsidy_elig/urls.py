from django.conf.urls import url
from .views import subelig, edit_subeligibility, delete_subeligibility

app_name = 'subsidy_elig'
urlpatterns = [
    url(r'^$', subelig, name='SubEligForms'),
    url(r'^edit-subeligibility/(?P<pk>\d+)$', edit_subeligibility, name='edit_subeligibility'),
    url(r'^delete-subpriority/(?P<pk>\d+)$', delete_subeligibility, name='delete_subeligibility'),

]
