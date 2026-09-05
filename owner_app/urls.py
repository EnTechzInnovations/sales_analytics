from django.urls import path,include
from . import views

urlpatterns = [

    path('owner_home',views.owner_home,name='owner_home'),
    path('owner_manage_branch',views.owner_manage_branch,name='owner_manage_branch'),
    path('owner_delete_branch/<id>',views.owner_delete_branch,name='owner_delete_branch'),
 
    
   
]
