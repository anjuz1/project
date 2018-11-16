from .views import chitfinaldraw
from django.conf.urls import url

app_name = 'chit_final_draw'
urlpatterns = [
    url(r'^chit_final/(?P<pk>\d+)$', chitfinaldraw, name='final')
]