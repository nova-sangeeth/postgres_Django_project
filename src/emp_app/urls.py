from django.conf.urls import url
from .views import index, employee_delete, employee_form, employee_list, edit_employee
urlpatterns = [
    url(r'^index$', index, name="index"),
    url(r'^empform$', employee_form, name="employee_form"),
    url(r'^emplist$', employee_list, name="employee_list"),

    # EDIT THE FORM URLS
    url(r'^editemp/(?P<pk>\d+)$', edit_employee, name='edit_employee')
    # url(r'^edit_laptop/(?P<pk>\d+)$', edit_laptop, name='edit_laptop'),

]
