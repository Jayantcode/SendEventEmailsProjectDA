
from django.contrib import admin
from django.urls import path
from django.conf import settings
from mail import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.send_email),
    path('send_emails/', views.send_emails)
]
