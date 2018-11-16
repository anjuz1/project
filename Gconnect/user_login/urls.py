from django.conf.urls import url
from .views import login, userhome

app_name = 'user_login'
urlpatterns = [
    url(r'^$', login, name='UserLoginForms'),
    url(r'^userhome', userhome, name='userhome')
]
