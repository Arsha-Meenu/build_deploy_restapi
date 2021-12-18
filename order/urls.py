from django.urls import path
from . import views

urlpatterns = [
    path('',views.OrderCreateListView.as_view(),name = 'orders_list'),
    path('<int:order_id>/',views.OrderDetailView.as_view(),name = 'order_details'),
    path('update-status/<int:order_id>/',views.UpdateOrderStatus.as_view(),name = 'order_status_update'),
    path('user/<int:user_id>/orders/',views.UserOrderListView.as_view(),name = "specific_user_order_list"),
    path('user/<int:user_id>/orders/<int:order_id>/',views.UserOrderDetail.as_view(),name = 'users_specification_detail1'),
    
]