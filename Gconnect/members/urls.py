from django.conf.urls import url
from .views import members, edit_member, delete_member

app_name = 'members'
urlpatterns = [
    url(r'^$', members, name='MemberForms'),
    url(r'^edit-member/(?P<pk>\d+)$', edit_member, name='edit_member'),
    url(r'^delete-member/(?P<pk>\d+)$', delete_member, name='delete_member'),

]
