from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='jubilee_health_insurance'),
]
