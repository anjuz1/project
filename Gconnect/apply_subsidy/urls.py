from .views import subsidy_application
from django.conf.urls import url

app_name = 'apply_subsidy'
urlpatterns = [
    url(r'^$', subsidy_application, name='ApplySubForms')
]