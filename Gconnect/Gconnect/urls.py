"""Gconnect URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^housename/', include('housename.urls')),
    url(r'^coordreg/', include('coordinator_reg.urls')),
    url(r'^place/', include('place.urls')),
    url(r'^subsidyelig/', include('subsidy_elig.urls')),
    url(r'^coordlogin/', include('coord_login.urls')),
    url(r'^coordchitdetails', include('chit_details.urls')),
    url(r'^coordchitinstall', include('chit_installment.urls')),
    #url(r'^wardmembreg/', include('wardmemb_reg.urls')),
    url(r'^wardlogin/', include('wardmemb_login.urls')),
    url(r'^chit/', include('chit.urls')),
    url(r'^meeting/', include('meeting.urls')),
    url(r'^subsidyprio/', include('subsidy_priority.urls')),
    url(r'^members/', include('members.urls')),
    url(r'^subsidytype/', include('subsidy_types.urls')),
    url(r'^chitmemb/', include('chit_members.urls')),
    url(r'^chit_final/', include('chit_final_install.urls')),
    url(r'^chit_drawmemb/', include('chit_draw_members.urls')),
    url(r'^chit_drawfinal/', include('chit_final_draw.urls')),
    url(r'^coordchitdraw', include('chit_draw.urls')),
    url(r'^userlogin/', include('user_login.urls')),
    url(r'^subdetail/', include('subsidy_details.urls')),
    url(r'^loandetail/', include('loan_details.urls')),
    url(r'^loanelig/', include('loan_elig.urls')),
    url(r'^loanprio/', include('loan_priority.urls')),
    url(r'^applysubsidy/', include('apply_subsidy.urls')),
    url(r'^attendance/', include('attendance.urls')),
    url(r'^gmeeting/', include('gmeeting.urls')),
    url(r'^viewsubsidy/', include('subsidy_view.urls')),
    url(r'^calcsubsidy/', include('subsidy_calc_priority.urls'))

]
