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
    path('admin_manage_category',views.admin_manage_category,name='admin_manage_category'),
    path('admin_delete_category/<id>',views.admin_delete_category,name='admin_delete_category'),
    path('admin_update_category/<id>',views.admin_update_category,name='admin_update_category'),
    path('admin_view_feedback',views.admin_view_feedback,name='admin_view_feedback'),
    path('admin_view_complaint',views.admin_view_complaint,name='admin_view_complaint'),
    path('admin_send_reply/<id>',views.admin_send_reply,name='admin_send_reply'),

    


   
]
