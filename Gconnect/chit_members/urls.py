from .views import chit_memb
from django.conf.urls import url

app_name = 'chit_members'
urlpatterns = [
    url(r'^chit_memb/(?P<pk>\d+)$', chit_memb, name='chit_memb')
]