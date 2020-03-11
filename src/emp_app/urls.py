from django.conf.urls import url
from .views import index, employee_delete, employee_form, employee_list
urlpatterns = [
    url(r'^index$', index, name="index"),
    url(r'^empform$', employee_form, name="employee_form"),
    url(r'^emplist$', employee_list, name="employee_list"),
    url(r'^empdelete$', employee_delete, name="employee_delete"),
]
