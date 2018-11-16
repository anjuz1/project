from django.conf.urls import url
from .views import chitinstallment

app_name = 'chit_installment'
urlpatterns = [
    url(r'^$', chitinstallment, name='ChitInstallmentForm')
]
