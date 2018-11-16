from django.conf.urls import url
from .views import gmeetings

app_name = 'gmeeting'
urlpatterns = [
    url(r'^$', gmeetings, name='gmeetings'),


]
