from django.urls import path
from . import views

urlpatterns = [
    path('login_users', views.login_users, name='login_users'),
    path('logout_users', views.logout_users, name='logout_users'),
    path('register_user', views.register_user, name='register_user'),
]
