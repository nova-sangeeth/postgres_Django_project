from django.conf.urls import url
# from django.urls import path, include
from .views import *
urlpatterns = [
    url(r'^$', index, name="index"),
    url(r'^employeeform$', employee_form, name="employee_form"),
    url(r'^employeeform/(?P<id>\d+)/$', employee_form, name="employee_update"),
    # url(r'^editemployee/(?P<pk>\d+)/$', addemployee, name='editemployee'),
    url(r'^employeelist$', employee_list, name="employee_list"),
    url(r'^delete/(?P<id>\d+)/$',
        employee_delete, name="employee_delete")
]
