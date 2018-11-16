from django.conf.urls import url
from .views import login, adminhome


app_name = 'wardmemb_login'

urlpatterns = [
    url(r'^$', login, name='Login_Ward_Forms'),
    url(r'^adminhome$', adminhome, name='adminhome'),
  #  url(r'^centerhome$', centerhome, name='centerhome'),

]