from django.conf.urls import url
from .views import subsidy_types, delete_subtypes, edit_subtypes

app_name = 'subsidy_types'
urlpatterns = [
    url(r'^$', subsidy_types, name='SubTypeForms'),
    url(r'^edit-subtypes/(?P<pk>\d+)$', edit_subtypes, name='edit_subtypes'),
    url(r'^delete-subtypes/(?P<pk>\d+)$', delete_subtypes, name='delete_subtypes'),

]
