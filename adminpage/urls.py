from django.urls import path
from .import views

urlpatterns = [
    path('logadmin/',views.logadmin,name='logadmin'),
    path('detail/<int:id>',views.datail,name='detail'),
    path('verified/<int:id>',views.verified,name='verified'),
    path('emp_list/',views.emp_list,name='emp_list'),
    path('pending_leave/',views.pending_leave,name='pending_leave'),
    path('approve_leave/',views.approve_leave,name='approve_leave'),
]