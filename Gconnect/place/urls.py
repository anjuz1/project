from django.conf.urls import url
from .views import places, edit_place, delete_place

app_name = 'place'
urlpatterns = [
    url(r'^$', places, name='PlaceForms'),
    url(r'^edit-place/(?P<pk>\d+)$', edit_place, name='edit_place'),
    url(r'^delete-place/(?P<pk>\d+)$', delete_place, name='delete_place'),

]
