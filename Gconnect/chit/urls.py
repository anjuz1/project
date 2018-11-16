from django.conf.urls import url
from .views import chits, edit_chit, delete_chit

app_name = 'chit'
urlpatterns = [
    url(r'^$', chits, name='ChitForms'),
    url(r'^edit-place/(?P<pk>\d+)$', edit_chit, name='edit_chit'),
    url(r'^delete-place/(?P<pk>\d+)$', delete_chit, name='delete_chit'),

]
