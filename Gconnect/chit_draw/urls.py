from django.conf.urls import url
from .views import chitdraw

app_name = 'chit_draw'
urlpatterns = [
    url(r'^$', chitdraw, name='ChitInstallmentForm')
]
