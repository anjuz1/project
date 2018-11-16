from django.conf.urls import url
from .views import wardmemb_reg

app_name = 'wardmemb_reg'
urlpatterns = [
    url(r'^$', wardmemb_reg, name='WardMembRegForms')
    ]
