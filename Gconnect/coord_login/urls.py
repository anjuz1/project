from django.conf.urls import url
from .views import login, coordhome

app_name = 'coord_login'
urlpatterns = [
    url(r'^$', login, name='LoginForms'),
    url(r'^coordhome', coordhome, name='coordhome')
]
