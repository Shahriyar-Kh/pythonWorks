from . import views
from django.urls import path
 

urlpatterns=[
    path('',views.main,name="main"),
    path("employees/",views.employees,name="employees"),
    path("employees/emp_details/<int:id>/",views.emp_details,name="emp_details"),
    path('testing',views.testing,name="testing"),
    path('student_data',views.student_data,name="student_data")
]