from django.conf.urls import url
from .views import attendance, memb_attendance

app_name = 'attendance'
urlpatterns = [
    url(r'^$', attendance, name='attendance'),
    url(r'^memb_count/(?P<pk>\d+)$', memb_attendance, name='memb_attendance')

]
