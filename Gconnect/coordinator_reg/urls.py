from django.conf.urls import url
from .views import coord_reg, edit_coordreg, delete_coordreg

app_name = 'coordinator_reg'
urlpatterns = [
    url(r'^$', coord_reg, name='CoordRegForms'),
    url(r'^edit-coord/(?P<pk>\d+)$', edit_coordreg, name='edit_coordreg'),
    url(r'^delete-coord/(?P<pk>\d+)$', delete_coordreg, name='delete_coordreg'),
]
