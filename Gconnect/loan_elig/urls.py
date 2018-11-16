from django.conf.urls import url
from .views import loanelig, edit_loaneligibility, delete_loaneligibility

app_name = 'loan_elig'
urlpatterns = [
    url(r'^$', loanelig, name='LoanEligForms'),
    url(r'^edit-loaneligibility/(?P<pk>\d+)$', edit_loaneligibility, name='edit_loaneligibility'),
    url(r'^delete-loanpriority/(?P<pk>\d+)$', delete_loaneligibility, name='delete_loaneligibility'),

]
