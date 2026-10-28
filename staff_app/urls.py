from django.urls import path,include
from . import views

urlpatterns = [

    path('staff_home',views.staff_home,name='staff_home'),
    path('staff_view_profile',views.staff_view_profile,name='staff_view_profile'),
    path('staff_send_complaint',views.staff_send_complaint,name='staff_send_complaint'),

    
    path('staff_record_sales', views.staff_record_sales, name='staff_record_sales'),

    path('staff_view_products', views.staff_view_products, name='staff_view_products'),

    path('staff_search_products', views.staff_search_products, name='staff_search_products'),

    path('staff_manage_customers', views.staff_manage_customers, name='staff_manage_customers'),

    path('staff_view_customer_details/<int:id>', views.staff_view_customer_details, name='staff_view_customer_details'),

    path('staff_view_daily_sales', views.staff_view_daily_sales, name='staff_view_daily_sales'),

    path('staff_view_takeaway_bookings', views.staff_view_takeaway_bookings, name='staff_view_takeaway_bookings'),

    path('staff_update_booking_status/<int:id>', views.staff_update_booking_status, name='staff_update_booking_status'),

    path('staff_customer_purchase_history/<int:id>',views.staff_customer_purchase_history,name='staff_customer_purchase_history'),


   
    
   
]
