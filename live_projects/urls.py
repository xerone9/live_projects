from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('class-scheduler/', include('class_scheduler.urls')),
    path('class-scheduler/members/', include('django.contrib.auth.urls')),
    path('class-scheduler/members/', include('members.urls')),
    path('amount_translator/', include('amount_translator.urls')),
    path('jubilee_insurance/', include('jubilee_insurance.urls')),
]
