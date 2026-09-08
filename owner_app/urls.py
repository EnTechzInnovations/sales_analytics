from django.urls import path,include
from . import views

urlpatterns = [

    path('owner_home',views.owner_home,name='owner_home'),
    path('owner_manage_branch',views.owner_manage_branch,name='owner_manage_branch'),
    path('owner_delete_branch/<id>',views.owner_delete_branch,name='owner_delete_branch'),
    path('owner_update_branch/<id>',views.owner_update_branch,name='owner_update_branch'),
    path('owner_manage_staff',views.owner_manage_staff,name='owner_manage_staff'),
    path('owner_delete_staff/<id>',views.owner_delete_staff,name='owner_delete_staff'),
    

 
    
   
]
