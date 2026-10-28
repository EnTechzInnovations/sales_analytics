from django.urls import path,include
from . import views

urlpatterns = [

    path('owner_home',views.owner_home,name='owner_home'),
    path('owner_manage_branch',views.owner_manage_branch,name='owner_manage_branch'),
    path('owner_delete_branch/<id>',views.owner_delete_branch,name='owner_delete_branch'),
    path('owner_update_branch/<id>',views.owner_update_branch,name='owner_update_branch'),
    path('owner_manage_staff',views.owner_manage_staff,name='owner_manage_staff'),
    path('owner_delete_staff/<id>',views.owner_delete_staff,name='owner_delete_staff'),
    path('owner_update_staff/<id>',views.owner_update_staff,name='owner_update_staff'),
    path('owner_manage_product',views.owner_manage_product,name='owner_manage_product'),
    path('owner_delete_product/<id>',views.owner_delete_product,name='owner_delete_product'),
    path('owner_update_product/<id>',views.owner_update_product,name='owner_update_product'),
    path('owner_send_compalint',views.owner_send_compalint,name='owner_send_compalint'),
    path('owner_send_feedback',views.owner_send_feedback,name='owner_send_feedback'),
    path('owner_view_profile',views.owner_view_profile,name='owner_view_profile'),
    path('owner_update_profile/<id>',views.owner_update_profile,name='owner_update_profile'),
    path('owner_view_customers',views.owner_view_customers,name='owner_view_customers'),

    
    
   
]
