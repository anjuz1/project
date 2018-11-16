from django.conf.urls import url
from .views import user_family_reg, edit_family, delete_family

app_name = 'housename'

urlpatterns = [
    url(r'^$', user_family_reg, name='HouseNameForms'),
    url(r'^edit-family/(?P<pk>\d+)$', edit_family, name='edit_family'),
    url(r'^delete-family/(?P<pk>\d+)$', delete_family, name='delete_family'),
]