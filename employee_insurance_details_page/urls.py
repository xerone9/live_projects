from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='employee_insurance_detail'),
]
