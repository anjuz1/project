from .views import chit_draw_memb
from django.conf.urls import url

app_name = 'chit_draw_members'
urlpatterns = [
    url(r'^chit_memb/(?P<pk>\d+)$', chit_draw_memb, name='chit_draw_memb')
]