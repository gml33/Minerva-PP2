from django.urls import path
from .views import home, register, my_login, user_logout, dashboard


urlpatterns = [
    path('',home,name=''),
    path('register',register, name='register'),
    path('my-login',my_login, name='my-login'),
    path('user-logout',user_logout, name='user-logout'),
    path('dashboard',dashboard, name='dashboard'),
    ]