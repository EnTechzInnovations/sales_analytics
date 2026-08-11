from django.urls import path,include
from . import views

urlpatterns = [

    path('',views.home,name='home'),
    path('login',views.login_section,name='login'),
    path('owner_register',views.owner_register,name='owner_register'),

    path('admin_home',views.admin_home,name='admin_home'),
    path('admin_view_onwer',views.admin_view_onwer,name='admin_view_onwer'),


   
]
