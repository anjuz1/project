from django.conf.urls import url
from .views import loan_prioritys, delete_loanpriority, edit_loanpriority

app_name = 'loan_priority'
urlpatterns = [
    url(r'^$', loan_prioritys, name='LoanPrioForms'),
    url(r'^edit-loanpriority/(?P<pk>\d+)$', edit_loanpriority, name='edit_loanpriority'),
    url(r'^delete-loanpriority/(?P<pk>\d+)$', delete_loanpriority, name='delete_loanpriority'),

]
