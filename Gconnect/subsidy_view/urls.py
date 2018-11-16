from django.conf.urls import url
from .views import ViewSubsidy

app_name = 'view_subsidy'
urlpatterns = [
    url(r'^$', ViewSubsidy, name='sub_view')
]
