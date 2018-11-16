from django.conf.urls import url
from .views import calc_priority

app_name = 'subsidy_calc_priority'
urlpatterns = [
    url(r'^calc_sub/(?P<pk>\d+)$', calc_priority, name='calc_priority')
]
