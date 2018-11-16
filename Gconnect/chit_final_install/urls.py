from .views import chitfinalinstallment
from django.conf.urls import url

app_name = 'chit_final_install'
urlpatterns = [
    url(r'^chit_final/(?P<pk>\d+)$', chitfinalinstallment, name='final')
]