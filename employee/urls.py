from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.index , name = 'index'),
    path('all_emp',views.all_emp , name = 'all_emp'),
    path('add_emp',views.add_emp , name = 'add_emp'),
    path('update_emp/<int:emp_id>',views.update_emp , name = 'update_emp'),
    path('remove_emp',views.remove_emp , name = 'remove_emp'),
    path('remove_emp_id/<int:emp_id>',views.remove_emp_id , name = 'remove_emp_id'),
    path('filter_emp',views.filter_emp , name = 'filter_emp'),

]