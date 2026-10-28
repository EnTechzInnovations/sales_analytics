from django.urls import path,include
from . import views

urlpatterns = [

    path("user_register",views.user_register,name='user_register'),
    path("user_login",views.user_login,name='user_login'),
    path("user_send_complaints",views.user_send_complaints,name='user_send_complaints'),
    path('User_view_complaints',views.User_view_complaints,name='User_view_complaints'),
    path('user_send_feedback',views.user_send_feedback,name='user_send_feedback'),
    path('updatepasslocation',views.updatepasslocation,name='updatepasslocation'),
    path('User_view_shops',views.User_view_shops,name='User_view_shops'),
    path('User_view_products',views.User_view_products,name='User_view_products'),
    path('User_add_book_to_take_away',views.User_add_book_to_take_away,name='User_add_book_to_take_away'),

    
    
   
]
