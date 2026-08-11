from django.urls import path,include
from . import views

urlpatterns = [

    path('',views.home,name='home'),
    path('login',views.login_section,name='login'),
    path('owner_register',views.owner_register,name='owner_register'),

    path('admin_home',views.admin_home,name='admin_home'),
    path('admin_view_owner',views.admin_view_owner,name='admin_view_owner'),
    path('admin_accept_owner/<id>',views.admin_accept_owner,name='admin_accept_owner'),
    path('admin_reject_owner/<id>',views.admin_reject_owner,name='admin_reject_owner'),
    path('admin_view_staff',views.admin_view_staff,name='admin_view_staff'),


   
]
