from django.urls import path
from . import views

urlpatterns = [
    path('',views.HelloView.as_view(),name = 'home'),
    path('signup/',views.UserCreationView.as_view(),name="sign_up"),
    path('users/',views.UserListView.as_view(),name="users_list")

]