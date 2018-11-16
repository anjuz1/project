from django.conf.urls import url
from .views import loan_details, delete_loandetails, edit_loandetails

app_name = 'loan_details'
urlpatterns = [
    url(r'^$', loan_details, name='LoanDetailsForms'),
    url(r'^edit-loandetail/(?P<pk>\d+)$', edit_loandetails, name='edit_loandetails'),
    url(r'^delete-loandetail(?P<pk>\d+)$', delete_loandetails, name='delete_loandetails'),

]
