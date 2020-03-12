from django.conf.urls import url
# from django.urls import path, include
from .views import *
urlpatterns = [
    url(r'^$', index, name="index"),
    url(r'^addemployee$', addemployee, name="addemployee"),
    # url(r'^editemployee/(?P<pk>\d+)/$', addemployee, name='editemployee'),
    url(r'^employee_list$', employee_list, name="employee_list"),

]
